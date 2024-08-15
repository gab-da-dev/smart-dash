<script lang="ts">
    import { getRequest, postRequest } from "$lib/services/http_service";
    import Input from "$lib/components/UI/Input.svelte";
    import TextArea from "$lib/components/UI/TextArea.svelte";
    import Checkbox from "$lib/components/UI/Checkbox.svelte";
    import DropDownSelect from "$lib/components/UI/DropDownSelect.svelte";
    import Number from "$lib/components/UI/Number.svelte";
    import validate from "validate.js";

    let errors = {};

    const productConstraints = {
        name: {
            presence: { allowEmpty: false, message: "^Name is required" },
        },
        active: {
            type: "boolean",
        },
        description: {
            presence: {
                allowEmpty: false,
                message: "^Description is required",
            },
        },
        image: {
            // You can add custom rules for image if needed
            presence: { allowEmpty: true }, // Allowing empty as per initial data structure
        },
        product_category_id: {
            presence: {
                allowEmpty: false,
                message: "^Product category is required",
            },
        },
        price: {
            numericality: {
                greaterThanOrEqualTo: 0,
                message: "^Price must be a positive number",
            },
        },
        prep_time: {
            numericality: {
                onlyInteger: true,
                greaterThanOrEqualTo: 0,
                message: "^Preparation time must be a non-negative integer",
            },
        },
        ingredients: {
            type: "array",
        },
    };

    // Product object
    let product = {
        name: "",
        active: true,
        description: "",
        image: null,
        product_category_id: "",
        price: 0,
        prep_time: 0,
        ingredients: [],
    };

    async function submit() {
        console.log(product);
        // return;
        errors = validate(product, productConstraints);
        if (errors) {
            console.error("Validation errors:", errors);
            return false; // Exit the function early if validation fails
        } else {
            errors = {};
        }
        try {
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

            if (product.ingredients) {
                formData.append("ingredients", product.ingredients);
            }

            // To see the appended formData values
            for (let pair of formData.entries()) {
                console.log(pair[0] + ", " + pair[1]);
            }

            // Send a POST request with the FormData
            const response = await postRequest("/product", formData, {
                "Content-Type": "multipart/form-data",
            });
            window.location.href = "/admin/products";
            // Log the response data
            console.log(response);

            // Return the items from the response data
            return response.items;
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

<div>
    <div>
        <Input
            label={"Name"}
            bind:input_value={product.name}
            {errors}
            element_id={"name"}
        /><br />
        <TextArea
            label={"Description"}
            bind:value={product.description}
            {errors}
            element_id={"description"}
        /><br />
        <Checkbox label={"Active"} bind:value={product.active} /><br />
        <!-- <Upload /><br /> -->
        {#await getRequest("/product-category/all") then value}
            <DropDownSelect
                data={value}
                bind:value={product.product_category_id}
                label={"Category"}
                {errors}
                element_id={"product_category_id"}
            />
        {/await}
        <br />
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
        <Number
            label={"Price"}
            bind:value={product.price}
            {errors}
            element_id={"price"}
        /><br />
        <Number
            label={"Preparation Time"}
            bind:value={product.prep_time}
            {errors}
            element_id={"prep_time"}
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
                                        id={ingredient.name}
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
                >Create</button
            >
        </div>
    </div>
</div>
