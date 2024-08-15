<script lang="ts">
    import { getRequest, postRequest } from "$lib/services/http_service";
    import Input from "$lib/components/UI/Input.svelte";
    import TextArea from "$lib/components/UI/TextArea.svelte";
    import Checkbox from "$lib/components/UI/Checkbox.svelte";
    import Upload from "$lib/components/UI/Upload.svelte";
    import DropDownSelect from "$lib/components/UI/DropDownSelect.svelte";
    import Button from "$lib/components/UI/Button.svelte";
    import validate from "validate.js";
    import Form from "$lib/components/UI/Form.svelte";
    import { onMount } from "svelte";

    export let data;
    let errors = {};

    // async function onMount() {
    //     alert('test')
    // }
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

    function validate_form() {
        console.error("Validation errors:", product);
        errors = validate(product, productConstraints) || {};
        let validationResult = validate(product, productConstraints);

        if (validationResult) {
            // Handle validation errors
            console.error("Validation errors:", validationResult, product);
            // // You can display errors to the user here, e.g., using alert or rendering errors on the page
            // alert("Validation failed. Please check the form for errors.");
            return false; // Exit the function early if validation fails
            alert("tests.");
        }
        return true;
    }

    async function submit() {
        alert("test");
        // Validate the product object
        // if (validate_form())

        // errors = validate(product, productConstraints) || {};
        // let validationResult = validate(product, productConstraints);

        // if (validationResult) {
        //     // Handle validation errors
        //     console.error("Validation errors:", validationResult, product);
        //     // // You can display errors to the user here, e.g., using alert or rendering errors on the page
        //     // alert("Validation failed. Please check the form for errors.");
        //     return false; // Exit the function early if validation fails

        // }

        try {
            // Send a POST request with the FormData
            const response = await postRequest("/product", product);
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

    function setProduct() {
        console.log(data);
        product = data;
    }

    onMount(() => {
        console.log(data);
        // setProduct();
    });
</script>

<div>
    <Form label="Edit Product" on:handleSubmit={submit}>
        <Input
            label={"Name"}
            value={product.name}
            {errors}
            element_id={"name"}
        /><br />
        <TextArea
            label={"Description"}
            value={product.description}
            {errors}
            element_id={"description"}
        /><br />
        <Checkbox label={"Active"} value={product.active} /><br />
        <!-- <Upload /><br /> -->
        {#await getRequest("/product-category/all") then value}
            <DropDownSelect
                data={value}
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
        <Input
            label={"Price"}
            value={product.price}
            type={"number"}
            {errors}
            element_id={"price"}
        /><br />
        <Input
            label={"Preparation Time"}
            value={product.prep_time}
            type={"number"}
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
    </Form>
</div>
