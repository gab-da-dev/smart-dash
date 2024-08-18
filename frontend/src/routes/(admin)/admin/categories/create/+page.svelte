<script>
  import Checkbox from "$lib/components/UI/Checkbox.svelte";
  import Form from "$lib/components/UI/Form.svelte";
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

    let errors = {};

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
            }

            // if (product.ingredients) {
            //     formData.append('ingredients', product.ingredients);
            // }

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

    <Form label={"Create category"} btn_label={"Create"} on:handleSubmit={()=>{
        submit()
    }}>
        
        <Input label={"Name"} bind:input_value={product.name} errors={errors} element_id={'name'}/><br />
        <TextArea label={"Description"} bind:value={product.description} errors={errors} element_id={'description'}/><br />
        <Checkbox label={"Active"} bind:value={product.active} /><br />
        <!-- <Upload /><br /> -->

        <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700">Image</label>
            <input type="file" name="image" on:change={handleFileInput}
                class="mt-1 block w-full text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        </div>

          
        </Form>