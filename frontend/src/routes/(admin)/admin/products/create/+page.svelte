<script>
    import { getRequest, postRequest } from "$lib/services/http_service";
    import { json, redirect } from "@sveltejs/kit";
    import Input from "$lib/components/UI/Input.svelte";
    import TextArea from "$lib/components/UI/TextArea.svelte";
    import Checkbox from "$lib/components/UI/Checkbox.svelte";
    import Upload from "$lib/components/UI/Upload.svelte";
    import DropDownSelect from "$lib/components/UI/DropDownSelect.svelte";
    let product = {
        name: "test",
        active: true,
        description: "test",
        image: null,
        product_category_id: "aaa0f3d1-339b-4a2d-acaa-092210823135",
        price: 2.3,
        prep_time: 5,
        ingredients: [],
    };

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
            console.log("FormData:", product);
            // Create a FormData object
            const formData = new FormData();

            // Append each key-value pair from the product object to the FormData object
            Object.entries(product).forEach(([key, value]) => {
                if (key === "ingredients") {
                    value.forEach((ingredient, index) => {
                        formData.append(`ingredients`, ingredient);
                    });
                } else if (key !== "image") {
                    formData.append(key, value);
                }
            });

            // Handle the image field separately if needed
            if (product.image) {
                formData.append("image", product.image);
                console.log("lalalala");
            }

            // if (product.ingredients) {
            //     formData.append('ingredients', product.ingredients);
            // }

            // To see the appended formData values
            for (let pair of formData.entries()) {
                console.log(pair[0] + ", " + pair[1]);
            }

            // Append the image file to the FormData object
            // formData.append('image', product.image);

            // Log the FormData object for debugging
            console.log("FormData:", formData);

            // Send a POST request with the FormData
            const response = await postRequest("/product", formData, {
                "Content-Type": "multipart/form-data",
            });

            // Log the response data
            console.log(response);

            // Return the items from the response data
            // redirect(302, '/products');
            window.location.href = "/admin/products";
        } catch (error) {
            // Handle any errors that occurred during the request
            console.error("Error submitting product:", error);
            throw error; // Rethrow the error if you want to propagate it further
        }
    }

    function handleFileInput(event) {
        const file = event.target.files[0];
        product.image = file;
    }
</script>

<svelte:head>
    <link rel="stylesheet" href="../../src/output.css" />
    <!-- CSS Theme -->
</svelte:head>
<div>
    <h2 class="text-2xl font-bold mb-4">Create Product</h2>
    <form action="/create-product" method="POST" enctype="multipart/form-data">
        <Input label={"Name"} value={product.name} /><br />
        <TextArea label={"Description"} value={product.description} /><br />
        <!-- <Checkbox label={"Active"} value={product.active} /> -->
        <Upload /><br />
        <DropDownSelect
            label={"Category"}
            value={product.product_category_id}
        /><br />
        <div class="mb-4">
            <label for="image" class="block text-sm font-medium text-gray-700"
                >Image</label
            >
            <input
                type="file"
                name="image"
                on:change={handleFileInput}
                class="mt-1 block w-full text-gray-900 border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
            />
        </div>
        <br />
        <Input label={"Price"} value={product.price} type={"number"} /><br />
        <Input
            label={"Preparation Time"}
            value={product.prep_time}
            type={"number"}
        /><br />

        <div class="mb-4">
            <div class="flex flex-col">
                {#await getRequest("/ingredient/all") then value}
                    <div class="flex flex-col">
                        <!-- <div class="flex-col"> -->
                        {#each value.items as ingredient}
                            <div class="flex items-start mb-6">
                                <div class="flex items-center h-5">
                                    <input
                                        id="remember"
                                        aria-describedby="remember"
                                        type="checkbox"
                                        name="active"
                                        value={ingredient.id}
                                        bind:group={product.ingredients}
                                        class="bg-gray-50 border-gray-300 focus:ring-3 focus:ring-blue-300 h-4 w-4 rounded"
                                        required=""
                                    />
                                </div>
                                <div class="text-sm ml-3">
                                    <label
                                        for="remember"
                                        class="font-medium text-gray-900 ml-4"
                                        >{ingredient.name}</label
                                    >
                                </div>
                            </div>
                        {/each}
                        <!-- </div> -->
                    </div>
                {/await}
            </div>
            <div class="flex flex-col"></div>
        </div>

        <div>
            <button
                on:click={submit}
                type="button"
                class="middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/40 active:opacity-[0.85] flex items-center gap-4 px-4 capitalize"
                >Create Product</button
            >
        </div>
    </form>
</div>
