<script>
  import Checkbox from "$lib/components/UI/Checkbox.svelte";
  import Input from "$lib/components/UI/Input.svelte";
  import TextArea from "$lib/components/UI/TextArea.svelte";
  import Upload from "$lib/components/UI/Upload.svelte";
    import {
        getRequest,
        postRequest
    } from "$lib/services/http_service";
    import {
        json
    } from "@sveltejs/kit";

    let product = {
        name: '',
        active: true,
        description: '',
        image: null,
    }


    async function submit() {
        try {
            console.log('FormData:', product);
            // Create a FormData object
            const formData = new FormData();

            // Append each key-value pair from the product object to the FormData object
            Object.entries(product).forEach(([key, value]) => {
                if (key !== 'image') {
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
            const response = await postRequest('/product-category', formData, {
                "Content-Type": "multipart/form-data",
            });

            window.location.href = "/admin/categories";


            // Return the items from the response data
            return response.items;
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
    <h2 class="text-2xl font-bold mb-6">Create Category</h2><br/>
    <form action="/create-product" method="POST" enctype="multipart/form-data">
        

        <Input label={"Name"} element_id={'name'} value={product.name} /><br />
        <TextArea label={"Description"} value={product.description} /><br />
        <Checkbox label={"Active"} value={product.active} />
        <!-- <Upload /><br /> -->

        <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
            <input type="file" name="image" on:change={handleFileInput}
                class="mt-1 block w-full text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

            <div>
                <button on:click={submit} type="button" class="text-xs py-3 rounded-lg bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/40 active:opacity-[0.85] w-full flex items-center gap-4 px-4 capitalize">Create Category</button>
            </div>
            
        </form>
    </div>