import { error } from '@sveltejs/kit';
import { getRequest } from '$lib/services/http_service.js';

export async function load({ params, fetch }) {
    console.log(params)
    const response = await fetch(`http://backend:5800/product/${params.slug}`);
    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }
    const data = await response.json();


    console.log(data)
    // if (!data) throw error(404);

    return {
        data
    };
}
