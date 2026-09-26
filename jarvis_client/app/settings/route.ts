import { NextRequest, NextResponse } from 'next/server';
import fs from 'fs';
import path from 'path';

// Server-side settings file — persists across clients on the same machine.
// Stored next to the Next.js standalone server so it survives builds.
function getSettingsPath(): string {
  // In production (Electron), write beside the bundled server.
  // In dev, write to project root so it's easy to inspect.
  const base =
    process.env.NODE_ENV === 'production'
      ? path.join(process.cwd())
      : path.join(process.cwd());
  return path.join(base, 'jarvis-server-settings.json');
}

function readSettings(): Record<string, unknown> {
  try {
    const p = getSettingsPath();
    if (!fs.existsSync(p)) return {};
    return JSON.parse(fs.readFileSync(p, 'utf-8')) as Record<string, unknown>;
  } catch {
    return {};
  }
}

function writeSettings(data: Record<string, unknown>): void {
  fs.writeFileSync(getSettingsPath(), JSON.stringify(data, null, 2), 'utf-8');
}

export async function GET() {
  const settings = readSettings();
  if (typeof settings.jarvis_settings === 'string') {
    try {
      const jarvis = JSON.parse(settings.jarvis_settings) as Record<string, unknown>;
      if (jarvis.openRouterKey) jarvis.openRouterKey = '__stored__';
      settings.jarvis_settings = JSON.stringify(jarvis);
    } catch { /* Keep malformed legacy data visible so it can be replaced. */ }
  }
  return NextResponse.json(settings);
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json() as Record<string, unknown>;
    // Merge with existing so partial updates (e.g. just HA creds) don't wipe everything
    const existing = readSettings();
    if (typeof body.jarvis_settings === 'string' && typeof existing.jarvis_settings === 'string') {
      try {
        const incoming = JSON.parse(body.jarvis_settings) as Record<string, unknown>;
        const current = JSON.parse(existing.jarvis_settings) as Record<string, unknown>;
        if (incoming.openRouterKey === '__stored__') incoming.openRouterKey = current.openRouterKey;
        body.jarvis_settings = JSON.stringify(incoming);
      } catch { /* Validation belongs to the settings UI; preserve legacy compatibility. */ }
    }
    const merged = { ...existing, ...body };
    writeSettings(merged);
    return NextResponse.json({ ok: true });
  } catch (err) {
    return NextResponse.json({ error: String(err) }, { status: 400 });
  }
}
