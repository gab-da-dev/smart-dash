<script>
    import Button from "$lib/components/UI/Button.svelte";
    import Checkbox from "$lib/components/UI/Checkbox.svelte";
    import Input from "$lib/components/UI/Input.svelte";
    import { getRequest, postRequest } from "$lib/services/http_service";
    import Number from "$lib/components/UI/Number.svelte";
    import validate from "validate.js";

    let errors = {};

    const productIngredientConstraints = {
        name: {
            presence: { allowEmpty: false, message: "^Name is required" },
        },
        active: {
            type: "boolean",
        },

        price: {
            numericality: {
                greaterThanOrEqualTo: 0,
                message: "^Price must be a positive number",
            },
        },
    };

    // Product object
    let product_ingredient = {
        name: "",
        active: true,
        price: 0,
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
            errors = validate(product_ingredient, productIngredientConstraints);

            if (errors) {
                console.error("Validation errors:", errors);
                return false; // Exit the function early if validation fails
            } else {
                errors = {};
            }
            // Send a POST request with the FormData
            const response = await postRequest(
                "/ingredient",
                product_ingredient,
            );
            window.location.href = "/admin/ingredients";
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
</script>

<div>
    <Input
        label={"Name"}
        bind:input_value={product_ingredient.name}
        {errors}
        element_id={"name"}
    /><br />
    <Checkbox label={"Active"} bind:value={product_ingredient.active} /><br />
    <Number
        label={"Price"}
        bind:value={product_ingredient.price}
        {errors}
        element_id={"price"}
    /><br />
    <div>
        <button
            on:click={submit}
            type="button"
            class="middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/40 active:opacity-[0.85] flex items-center gap-4 px-4 capitalize"
            >Create</button
        >
    </div>
</div>
