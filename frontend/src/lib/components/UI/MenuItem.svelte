<script>
import { createEventDispatcher } from 'svelte';

export let name = '';
export let price = '';
export let product_ingredients = [];
const dispatch = createEventDispatcher();

function view_product() {
    dispatch('viewProduct');
}

function getIngredientNames(data) {
    return data.map(item => item.ingredient.name).join(', ');;
}


</script>

<!-- Menu Item -->
<div class="menu-item menu-list-item">
    <div class="row align-items-center">
        <div class="col-sm-6 mb-2 mb-sm-0">
            <h6 class="mb-0">{name}</h6>
            <span class="text-muted text-sm">{getIngredientNames(product_ingredients)}</span>
        </div>
        <div class="col-sm-6 text-sm-right">
            <span class="text-md mr-4"><span class="text-muted">from</span> R<span data-product-base-price>{price}</span></span>
            <button class="btn btn-outline-secondary btn-sm" data-action="open-cart-modal" data-id="2" on:click={view_product}><span>Add to cart</span></button>
        </div>
    </div>
</div>