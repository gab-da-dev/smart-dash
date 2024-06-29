<script>
  import { getRequest, postRequest } from "$lib/services/http_service";
  import { json } from "@sveltejs/kit";

 let product = {
    name: '',
    active: '',
    description: '',
    image: '',
    product_category_id:'',
    price: '',
    prep_time: ''
}

async function submit() {
    console.log(json(product))
    await postRequest(`/product`, json(product))
  .then(data => {
    console.log(data)
    return data.items;
    
  });
}

</script>

    <div class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-lg">
        <h2 class="text-2xl font-bold mb-6">Create Product</h2>
        <form action="/create-product" method="POST" enctype="multipart/form-data">
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" name="name" bind:value={product.name} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label for="active" class="block text-sm font-medium text-gray-700">Active</label>
                <input type="checkbox" name="active" bind:value={product.active} class="mt-1 block rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                <textarea name="description" bind:value={product.description} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
            </div>

            <div class="mb-4">
                <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
                <input type="file" name="image" bind:value={product.image} class="mt-1 block w-full text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label for="product_category_id" class="block text-sm font-medium text-gray-700">Product Category ID</label>
                <input type="text" name="product_category_id" bind:value={product.product_category_id} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
                <input type="number" step="0.01" name="price" bind:value={product.price} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label for="prep_time" class="block text-sm font-medium text-gray-700">Preparation Time</label>
                <input type="text" name="prep_time" bind:value={product.prep_time} class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
            </div>

            <div class="mb-4">
                <label class="block text-sm font-medium text-gray-700">Ingredients</label>
                <div id="ingredient-container"></div>
                <button type="button" onclick="addIngredientField()" class="mt-2 bg-blue-500 text-white px-4 py-2 rounded-md shadow-sm hover:bg-blue-700">Add Ingredient</button>
            </div>

            <div>
                <button on:click={submit} type="button" class="w-full bg-green-500 text-black px-4 py-2 rounded-md shadow-sm hover:bg-green-700">Create Product</button>
            </div>
        </form>
    </div>
