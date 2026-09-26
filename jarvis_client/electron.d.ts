export {};
declare global {
  interface Window {
    electron?: {
      isElectron: boolean;
      platform: string;
      setDesktopMode: (options: {enabled: boolean; position?: string; logo?: string; muted?: boolean}) => Promise<unknown>;
      moveDesktopPanel: (position: string) => Promise<unknown>;
      setDesktopPanelMuted: (muted: boolean) => void;
      setDesktopPanelMousePassthrough: (passthrough: boolean) => void;
      overlayClick: () => void;
      getAudioSourceId: () => Promise<string>;
      onDesktopOverlayClick: (callback: () => void) => () => void;
      onDesktopPanelMuted: (callback: (muted: boolean) => void) => () => void;
      onMenuAction: (callback: (action: string) => void) => () => void;
    };
  }
}
