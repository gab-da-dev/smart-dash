<script>
    import CartItem from "$lib/components/UI/CartItem.svelte";
</script>

<!-- Panel Cart -->
<div id="panel-cart">
    <div class="panel-cart-container">
        <div class="panel-cart-title">
            <h5 class="title">Your Cart</h5>
            <button class="close" data-toggle="panel-cart"><i class="ti ti-close"></i></button>
        </div>
        <div class="panel-cart-content cart-details">
            <table class="cart-table">
                <CartItem></CartItem>
                <CartItem></CartItem>
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