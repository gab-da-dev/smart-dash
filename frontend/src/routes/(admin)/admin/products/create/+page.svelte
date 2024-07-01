<script>
    import {
        getRequest,
        postRequest
    } from "$lib/services/http_service";
    import {
        json,

        redirect

    } from "@sveltejs/kit";

    let product = {
        name: 'test',
        active: true,
        description: 'test',
        image: null,
        product_category_id: 'aaa0f3d1-339b-4a2d-acaa-092210823135',
        price: 2.3,
        prep_time: 5,
        ingredients: []
    }

    // async function submit() {
    //     console.log(JSON.stringify(product))
    //     await postRequest(`/product`, JSON.stringify(product))
    //   .then(data => {
    //     console.log(data)
    //     return data.items;

    //   });
    // }

    async function submit() {
        try {
            console.log('FormData:', product);
            // Create a FormData object
            const formData = new FormData();

            // Append each key-value pair from the product object to the FormData object
            Object.entries(product).forEach(([key, value]) => {
                if (key === 'ingredients') {
                    value.forEach((ingredient, index) => {
                        formData.append(`ingredients`, ingredient);
                    });
                } else if (key !== 'image') {
                    formData.append(key, value);
                }
            });

            // Handle the image field separately if needed
            if (product.image) {
                formData.append('image', product.image);
                console.log('lalalala')
            }

            // if (product.ingredients) {
            //     formData.append('ingredients', product.ingredients);
            // }

            // To see the appended formData values
            for (let pair of formData.entries()) {
                console.log(pair[0]+ ', ' + pair[1]); 
            }

            // Append the image file to the FormData object
            // formData.append('image', product.image);

            // Log the FormData object for debugging
            console.log('FormData:', formData);

            // Send a POST request with the FormData
            const response = await postRequest('/product', formData,{
                "Content-Type": "multipart/form-data",
            });

            // Log the response data
            console.log(response);

            
            // Return the items from the response data
            // redirect(302, '/products');
            window.location.href = "/admin/products";

        } catch (error) {
            // Handle any errors that occurred during the request
            console.error('Error submitting product:', error);
            throw error; // Rethrow the error if you want to propagate it further
        }
    }

    function handleFileInput(event) {
        const file = event.target.files[0];
        product.image = file;
    }
</script>

<svelte:head>
    <link rel="stylesheet" href="../../src/output.css"/>
    <!-- CSS Theme -->
</svelte:head>
<div class="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold mb-6">Create Product</h2>
    <form action="/create-product" method="POST" enctype="multipart/form-data">
        <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input type="text" name="name" bind:value={product.name}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">
            <label for="active" class="block text-sm font-medium text-gray-700">Active</label>
            <input type="checkbox" name="active" bind:checked={product.active}
                class="mt-1 block rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea name="description" bind:value={product.description}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
        </div>

        <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
            <input type="file" name="image" on:change={handleFileInput}
                class="mt-1 block w-full text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">
            <label for="product_category_id" class="block text-sm font-medium text-gray-700">Product Category</label>
            <input type="text" name="product_category_id" bind:value={product.product_category_id}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">
            <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
            <input type="number" step="0.01" name="price" bind:value={product.price}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">
            <label for="prep_time" class="block text-sm font-medium text-gray-700">Preparation Time</label>
            <input type="text" name="prep_time" bind:value={product.prep_time}
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

        <div class="mb-4">

            <div class="flex flex-col">
                {#await getRequest('/ingredient/all') then value}
                    <div class="flex flex-col">
                        <!-- <div class="flex-col"> -->
                            {#each value.items as ingredient}
                            <div class="flex items-start mb-6">
                                <div class="flex items-center h-5">
                                    <input id="remember" aria-describedby="remember" type="checkbox" name="active" value={ingredient.id} bind:group={product.ingredients} class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded" required="">
                                </div>
                                <div class="text-sm ml-3">
                                <label for="remember" class="font-medium text-gray-900 ml-4">{ingredient.name}</label>
                                </div>
                            </div>

                                {/each}
                        <!-- </div> -->
                        
                    </div>
                {/await}
            </div>
            <div class="flex flex-col">

            </div>
        </div>
                
            <div>
                <button on:click={submit} type="button" class="w-full bg-green-500 text-black px-4 py-2 rounded-md shadow-sm hover:bg-green-700">Create Product</button>
            </div>
            
        </form>
    </div>