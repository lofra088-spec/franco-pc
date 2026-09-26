import { providerSettings, checkOrigin } from '../../lib/provider-server';

export async function POST(req: Request) {
  try {
    checkOrigin(req);
    const settings = await providerSettings();
    if (settings.apiMode !== 'openrouter' || !settings.openRouterKey?.trim()) {
      return Response.json({error: 'Configura e salva la chiave OpenRouter nelle impostazioni.'}, {status: 400});
    }
    const {messages, tools} = await req.json();
    if (!Array.isArray(messages) || messages.length > 150 || JSON.stringify(messages).length > 200000) {
      return Response.json({error: 'Conversazione troppo lunga: disconnetti e riattiva Jarvis.'}, {status: 400});
    }
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {'Authorization': `Bearer ${settings.openRouterKey.trim()}`, 'Content-Type': 'application/json', 'X-Title': 'Jarvis'},
      body: JSON.stringify({model: settings.openRouterModel?.trim() || 'openrouter/auto', messages: [{role: 'system', content: settings.initialPrompt || 'Sei Jarvis. Rispondi in italiano.'}, ...messages], ...(Array.isArray(tools) && tools.length ? {tools} : {})}),
      signal: AbortSignal.any([req.signal, AbortSignal.timeout(120000)]),
    });
    const data = await response.json();
    if (!response.ok || data.error) return Response.json({error: `OpenRouter: ${data.error?.message || response.status}`}, {status: 502});
    const message = data.choices?.[0]?.message;
    if (!message) throw new Error('OpenRouter non ha restituito una risposta.');
    return Response.json({message});
  } catch (error) {
    return Response.json({error: error instanceof Error ? error.message : 'Errore nella conversazione'}, {status: 500});
  }
}
