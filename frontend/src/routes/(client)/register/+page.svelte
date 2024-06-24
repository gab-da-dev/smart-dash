<script lang="ts">
    import Cart from "$lib/components/UI/Cart.svelte";
import Header from "$lib/components/UI/Header.svelte";
import MenuItem from "$lib/components/UI/MenuItem.svelte";
import Modal from "$lib/components/UI/Modal.svelte";
import MenuCategory from "$lib/components/UI/MenuCategory.svelte";
  
let modal_show = false;
let cart_show = false;
let categories:[]
let cart:[];
let product;
let additional_ingredients;
let body_overlay = false



    let user = {
        first_name: "string",
        last_name: "string",
        phone_number: "string",
        email: "string",
        password: "string"
}
</script>
<svelte:head>
    <link rel="stylesheet" type="text/css" href="http://localhost:5173/css/core.css"/>
    <!-- CSS Theme -->
    <link id="theme" rel="stylesheet" href="http://localhost:5173/css/theme-beige.css" />
</svelte:head>



<!-- Body Wrapper -->
<div id="body-wrapper" class="animsition_">

    <Header on:viewCart={() => {
        cart_show = true;
        body_overlay = true;
        
    }}></Header>

    <!-- Header / End -->

    <!-- Header -->
    <header id="header-mobile" class="light">

        <div class="module module-nav-toggle">
            <a href="#" id="nav-toggle" data-toggle="panel-mobile"><span></span><span></span><span></span><span></span></a>
        </div>

        <div class="module module-logo">
            <a href="index.html">
                <img src="assets/img/logo-horizontal-dark.svg" alt="">
            </a>
        </div>

        <a href="#" class="module module-cart" data-toggle="panel-cart">
            <i class="ti ti-shopping-cart"></i>
            <span class="notification">0</span>
        </a>

    </header>
    <!-- Header / End -->

    <!-- Content -->
    <div id="content">

        <!-- Section -->
        <section class="section section-lg bg-light">

            <!-- Video BG -->

            <!-- BG Video -->
            <!-- <div class="bg-video dark-overlay" data-src="http://assets.suelo.pl/soup/video/video_3.mp4" data-type="video/mp4"></div> -->

            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-6">
                        <!-- Book a Table -->
                        <div class="utility-box">
                            <div class="utility-box-title bg-dark dark">
                                <div class="bg-image"><img src=http://localhost:5173/img/shesha-logos_white.png alt=""></div>
                                <div>
                                    <h4 class="mb-0">Register</h4>
                                    <p class="lead text-muted mb-0">Create user account.</p>
                                </div>
                            </div>
                            <form action="#" id="booking-form" class="booking-form" data-validate>
                                <div class="utility-box-content">
                                    <div class="form-group">
                                        <label>First name:</label>
                                        <input type="text" name="first_name" class="form-control" required bind:value={user.first_name}>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control">Last name:</label>
                                        <input type="text" name="last_name" class="form-control" required bind:value={user.last_name}>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control">E-mail:</label>
                                        <input type="email" name="email" class="form-control" required bind:value={user.email}>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control">Phone:</label>
                                        <input type="text" name="phone_number" class="form-control" required bind:value={user.phone_number}>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control">Password:</label>
                                        <input type="password" name="password" class="form-control" required bind:value={user.password}>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control">Confirm password:</label>
                                        <input type="password" name="password" class="form-control" required bind:value={user.password}>
                                    </div>
                                    
                                </div>
                                <button class="utility-box-btn btn btn-secondary btn-block btn-lg btn-submit" type="submit">
                                    <span class="description">Register</span>
                                    <span class="success">
                                        <svg x="0px" y="0px" viewBox="0 0 32 32"><path stroke-dasharray="19.79 19.79" stroke-dashoffset="19.79" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="square" stroke-miterlimit="10" d="M9,17l3.9,3.9c0.1,0.1,0.2,0.1,0.3,0L23,11"/></svg>
                                    </span>
                                    <span class="error">Try again...</span>
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

        </section>

      

    </div>
    <!-- Content / End -->


    <!-- Body Overlay -->
    <div id="body-overlay"></div>

</div>
