import type {NextConfig} from 'next';
const config: NextConfig = {output: 'standalone', outputFileTracingRoot: process.cwd(), serverExternalPackages: ['@jitsi/robotjs','screenshot-desktop','sharp']};
export default config;
