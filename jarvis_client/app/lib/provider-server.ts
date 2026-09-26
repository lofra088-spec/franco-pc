import fs from 'node:fs/promises';
import path from 'node:path';

export async function providerSettings() {
  let data: {jarvis_settings?: string} = {};
  try {
    data = JSON.parse(await fs.readFile(path.join(process.cwd(), 'jarvis-server-settings.json'), 'utf8'));
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code !== 'ENOENT') throw error;
  }
  return JSON.parse(data.jarvis_settings || '{}');
}

export function localVoiceUrl(value: string = 'http://127.0.0.1:8020') {
  const url = new URL(value);
  if (url.protocol !== 'http:' || !['127.0.0.1', 'localhost', '[::1]'].includes(url.hostname) || url.username || url.password) {
    throw new Error('Il servizio vocale deve usare http su localhost.');
  }
  return url.origin;
}

export function checkOrigin(req: Request) {
  const origin = req.headers.get('origin');
  if (origin && new URL(origin).host !== req.headers.get('host')) throw new Error('Origine non autorizzata');
}
