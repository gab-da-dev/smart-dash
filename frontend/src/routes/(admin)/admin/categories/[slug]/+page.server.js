
/** @type {import('./$types').PageServerLoad} */
export async function load({ params, fetch }) {
    console.log(params)
    const response = await fetch(`http://backend:8000/product-category/${params.slug}`);
    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }
    const data = await response.json();


    // if (!data) throw error(404);

    return data;
}
