import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from 'path';
const host = process.env.TAURI_pnpmDEV_HOST;

// https://vitejs.dev/config/
export default defineConfig(async () => ({
  plugins: [vue()],
  // Vite options tailored for Tauri development and only applied in `tauri dev` or `tauri build`
  //
  // 1. prevent vite from obscuring rust errors
  clearScreen: false,
    optimizeDeps: {
        include: ['tailwindcss', 'autoprefixer'],
    },
  // 2. tauri expects a fixed port, fail if that port is not available
  server: {
    port: 1420,
    strictPort: true,
    host: host || false,
    hmr: host
      ? {
          protocol: "ws",
          host,
          port: 1421,
        }
      : undefined,
    watch: {
      // 3. tell vite to ignore watching `src-tauri`
      ignored: ["**/src-tauri/**"],
    },
  },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, 'src'),
        }
    }
}));
