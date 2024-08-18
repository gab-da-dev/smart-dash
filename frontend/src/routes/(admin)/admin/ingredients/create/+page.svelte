<script>
    import Button from "$lib/components/UI/Button.svelte";
    import Checkbox from "$lib/components/UI/Checkbox.svelte";
    import Input from "$lib/components/UI/Input.svelte";
    import { getRequest, postRequest } from "$lib/services/http_service";
    import Number from "$lib/components/UI/Number.svelte";
    import validate from "validate.js";
  import Form from "$lib/components/UI/Form.svelte";

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

            // Return the items from the response data
            return response.items;
        } catch (error) {
            // Handle any errors that occurred during the request
            console.error("Error submitting product:", error);
            throw error; // Rethrow the error if you want to propagate it further
        }
    }
</script>

<Form label={"Create ingredient"} btn_label={"Create"} on:handleSubmit={()=>{
    submit()
}}>
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
   
</Form>
