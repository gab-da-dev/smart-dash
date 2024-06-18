<script lang="ts">
    import CartItem from "$lib/components/UI/CartItem.svelte";
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();
    function handleCloseCart() {
        dispatch('closeCart');
    }

    export let cart:[any] = [{
      "product_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "note": "string"
    }];
</script>

<!-- Panel Cart -->
<div id="panel-cart" class="show">
    <div class="panel-cart-container">
        <div class="panel-cart-title">
            <h5 class="title">Your Cart</h5>
            <button class="close" data-toggle="panel-cart" on:click={handleCloseCart}><i class="ti ti-close"></i></button>
        </div>
        <div class="panel-cart-content cart-details">
            <table class="cart-table">
                {#each cart as obj}
                    <CartItem></CartItem>
                {/each}
                
            </table>
            <div class="cart-summary">
                <div class="row">
                    <div class="col-7 text-right text-muted">Order total:</div>
                    <div class="col-5"><strong>$<span class="cart-products-total">0.00</span></strong></div>
                </div>
                <div class="row">
                    <div class="col-7 text-right text-muted">Devliery:</div>
                    <div class="col-5"><strong>$<span class="cart-delivery">0.00</span></strong></div>
                </div>
                <hr class="hr-sm">
                <div class="row text-lg">
                    <div class="col-7 text-right text-muted">Total:</div>
                    <div class="col-5"><strong>$<span class="cart-total">0.00</span></strong></div>
                </div>
            </div>
            <div class="cart-empty">
                <i class="ti ti-shopping-cart"></i>
                <p>Your cart is empty...</p>
            </div>
        </div>
    </div>
    <a href="checkout.html" class="panel-cart-action btn btn-secondary btn-block btn-lg"><span>Go to checkout</span></a>
</div>