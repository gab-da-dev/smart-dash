<script lang="ts">
  import { getRequest } from '$lib/services/http_service';


import { createEventDispatcher } from 'svelte';

 let additional_ingredients;
export let product;
let cart;
let order_item = {
    additional_ingredient: [],
    note: "",
    product_size_id: ""
};

 // Function to update the ingredientIds array based on checkbox state
 function updateIngredientIds(id, checked) {
        if (checked) {
            // Add the id if the checkbox is checked
            if (!order_item.additional_ingredient.includes(id)) {
                order_item.additional_ingredient = [...order_item.additional_ingredient, id];
            }
        } else {
            // Remove the id if the checkbox is unchecked
            order_item.additional_ingredient = order_item.additional_ingredient.filter(item => item !== id);
        }
        console.log(order_item)
    }

const dispatch = createEventDispatcher();

function handleClose() {
    dispatch('closeModal');
}

function getIngredientNames(data) {
    return data.map(item => item.ingredient.name).join(', ');;
}

async function init_data() {
     await getRequest(`/ingredient/all`)
  .then(data => {
    console.log(data.items,'yesr')
    additional_ingredients = data.items;
    
  });
}
function toggle_menu() {
    console.log(order_item)
}
</script>

<!-- Modal / Product -->
<!-- {#await init_data()} -->
<div class="modal fade product-modal show" id="product-modal" role="dialog" style="display: block;">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header modal-header-lg dark bg-dark">
                <div class="bg-image" style='background-image: url("http://localhost:5173/img/kota.jpg");'><img src="http://localhost:5173/img/Bunny_chow.jpg" alt=""></div>
                <h4 class="modal-title">Specify your dish</h4>
                <button type="button" on:click={handleClose} class="close" data-dismiss="modal" aria-label="Close"><i class="ti ti-close"></i></button>
            </div>
            <div class="modal-product-details">
                <div class="row align-items-center">
                    <div class="col-9">
                        <h6 class="mb-1 product-modal-name">{product.name}</h6>
                        <span class="text-muted product-modal-ingredients">{getIngredientNames(product.product_ingredients)}</span>
                    </div>
                    <div class="col-3 text-lg text-right">R<span class="product-modal-price">{product.price}</span></div>
                </div>
            </div>
            <div class="modal-body panel-details-container">
                <!-- Panel Details / Size -->
                <div class="panel-details panel-details-size">
                    <h5 class="panel-details-title">
                        <label class="custom-control custom-radio">
                            <input name="radio_title_size" type="radio" class="custom-control-input">
                            <span class="custom-control-indicator"></span>
                        </label>
                        <a href="#panel-details-sizes-list" data-toggle="collapse">Size</a>
                    </h5>
                    {#if product.product_size.length > 0}
                    <div id="panel-details-sizes-list" class="collapse show">
                        <div class="panel-details-content">
                            <div class="product-modal-sizes">
                                {#each product.product_size as product_size}
                                <div class="form-group">
                                    <label class="custom-control custom-radio">
                                        <input name="radio_size" type="radio" class="custom-control-input" value={product_size.id} bind:group={order_item.product_size_id}>
                                        <span class="custom-control-indicator"></span>
                                        <span class="custom-control-description">{product_size.name} (R{product_size.price})</span>
                                    </label>
                                </div>
                                {/each}
                                
                            </div>
                        </div>
                    </div>
                    {/if}
                </div>
                <!-- Panel Details / Additions -->
                <div class="panel-details panel-details-additions">
                    <h5 class="panel-details-title">
                        <label class="custom-control custom-radio">
                            <input name="radio_title_additions" type="radio" class="custom-control-input">
                            <span class="custom-control-indicator"></span>
                        </label>
                        <a href="#panel-details-additions-content" data-toggle="collapse">Additions</a>
                    </h5>
                    <div id="panel-details-additions-content" class="collapse show">
                        <div class="panel-details-content">
                            <!-- Additions List -->
                            <div class="row product-modal-additions">
                                <div class="col-sm-6">
                                    {#await getRequest('ingredient/all') then value}
                                        {#each value.items as additional_ingredient}
                                            <div class="form-group">
                                                <label class="custom-control custom-checkbox">
                                                    <input name="test" type="checkbox" value={additional_ingredient.id} class="custom-control-input" on:change="{(e) => updateIngredientIds(additional_ingredient.id, e.target.checked)}">
                                                    <span class="custom-control-indicator"></span>
                                                    <span class="custom-control-description">{additional_ingredient.name} R{additional_ingredient.price}</span>
                                                </label>
                                            </div>
                                        {/each}
                                    {/await}
                                   
                                    
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Panel Details / Other -->
                <div class="panel-details panel-details-form">
                    <h5 class="panel-details-title">
                        <label class="custom-control custom-radio">
                            <input name="radio_title_other" type="radio" class="custom-control-input">
                            <span class="custom-control-indicator"></span>
                        </label>
                        <a href="#panel-details-other" data-toggle="collapse">Note</a>
                    </h5>
                    <div id="panel-details-other" class="collapse show">
                        <form action="#">
                            <textarea cols="30" rows="4" class="form-control" placeholder="Put this any other informations..." bind:value={order_item.note}></textarea>
                        </form>
                    </div>
                </div>
            </div>
            <button type="button" on:click={toggle_menu} class="modal-btn btn btn-secondary btn-block btn-lg" data-action="add-to-cart"><span>Add to Cart</span></button>
            <button type="button" class="modal-btn btn btn-secondary btn-block btn-lg" data-action="update-cart"><span>Update</span></button>
        </div>
    </div>
</div>
<!-- {/await} -->