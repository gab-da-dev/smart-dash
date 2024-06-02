import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
	server: {
		allow: ['/home/gabriel/smart-dash/frontend/assets/'], // Add the directory path
	  },
	plugins: [sveltekit()],
	resolve: {
		alias: {
		  $assets: path.resolve(__dirname, 'assets/'),
		//   $lib: path.resolve(__dirname, 'src/lib/'),
		//   $app: path.resolve(__dirname, 'src/mocks/app')
	
		},
	  }
});
