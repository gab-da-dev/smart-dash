<script lang="ts">
import Cart from "$lib/components/UI/Cart.svelte";
import Header from "$lib/components/UI/Header.svelte";
import MenuItem from "$lib/components/UI/MenuItem.svelte";
import Modal from "$lib/components/UI/Modal.svelte";
import MenuCategory from "$lib/components/UI/MenuCategory.svelte";
  
import { createEventDispatcher } from 'svelte';
import { getRequest } from '$lib/services/http_service';

let modal_show = false;
let categories:[]

const dispatch = createEventDispatcher();

function view_product() {
    modal_show = true;
}


async function getCategoryProducts() {
    getRequest('product-category/all')
  .then(data => {
    categories = data.items;
    
    console.log(categories.length);
  });
}
</script>

<svelte:head>
    <link rel="stylesheet" type="text/css" href="http://localhost:5173/css/core.css"/>
    <!-- CSS Theme -->
    <link id="theme" rel="stylesheet" href="http://localhost:5173/css/theme-beige.css" />
</svelte:head>


    <!-- Body Wrapper -->
    <div id="body-wrapper" class="animsition-">
    
        
        <Header></Header>
    
        
    
        <!-- Content -->
        <div id="content">
    
            <!-- Page Title -->
            <div class="page-title bg-light">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 offset-lg-4">
                            <h1 class="mb-0">Buzz Kota's</h1>
                            <h4 class="text-muted mb-0">Some informations about our restaurant</h4>
                        </div>
                    </div>
                </div>
            </div>
    
            <!-- Page Content -->
            <div class="page-content">
                <div class="container">
                    <div class="row no-gutters">
                        <div class="col-md-10 offset-md-1" role="tablist">
                            <!-- Menu Category / Burgers -->
                            {#await getRequest('product-category/all-categories-with-products') then value}
                                {#each value.items as category}
                                    <MenuCategory on:viewProduct={() => {
                                        modal_show = true;
                                    }} title={category.name} category_id={category.name} products={category.products}></MenuCategory>

                                {/each}
                            {/await}
                            
                            <!-- Menu Category / Pasta -->
                            <div id="Pasta" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuPastaContent" data-toggle="collapse" aria-expanded="true">
                                    <div class="bg-image" style='background-image: url("http://localhost:5173/img/kota.jpg");'><img src="http://localhost:5173/img/kota.jpg" alt=""></div>
                                    <h2 class="title">Pasta</h2>
                                </div>
                                <div id="menuPastaContent" class="menu-category-content collapse">
                                    <MenuItem
                                    on:viewProduct={() => {
                                        modal_show = true;
                                    }}
                                    ></MenuItem>
                                </div>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
    
    
        </div>
        <!-- Content / End -->
    
        
        <Cart/>
        <!-- Panel Mobile -->
        <nav id="panel-mobile">
            <div class="module module-logo bg-dark dark">
                <a href="#test">
                    <img src=/img/logo-light.svg alt="" width="88">
                </a>
                <button class="close" data-toggle="panel-mobile"><i class="ti ti-close"></i></button>
            </div>
            <nav class="module module-navigation"></nav>
            <div class="module module-social">
                <h6 class="text-sm mb-3">Follow Us!</h6>
                <a href="#test" class="icon icon-social icon-circle icon-sm icon-facebook"><i class="fa fa-facebook"></i></a>
                <a href="#test" class="icon icon-social icon-circle icon-sm icon-google"><i class="fa fa-google"></i></a>
                <a href="#test" class="icon icon-social icon-circle icon-sm icon-twitter"><i class="fa fa-twitter"></i></a>
                <a href="#test" class="icon icon-social icon-circle icon-sm icon-youtube"><i class="fa fa-youtube"></i></a>
                <a href="#test" class="icon icon-social icon-circle icon-sm icon-instagram"><i class="fa fa-instagram"></i></a>
            </div>
        </nav>
    
        <!-- Body Overlay -->
        <div id="body-overlay"></div>
    
    </div>
    {#if modal_show}
        <Modal 
            on:closeModal={() => {
                modal_show = !modal_show;
            }}
            on:viewProduct={() => {
                modal_show = true;
                alert('test')
            }}
            >
            </Modal>
    {/if}
    <!-- Cookies Bar -->
    <div id="cookies-bar" class="body-bar cookies-bar">
        <div class="body-bar-container container">
            <div class="body-bar-text">
                <h4 class="mb-2">Cookies & GDPR</h4>
                <p>This is a sample Cookies / GDPR information. You can use it easily on your site and even add link to <a href="#test">Privacy Policy</a>.</p>
            </div>
            <div class="body-bar-action">
                <button class="btn btn-primary" data-accept="cookies"><span>Accept</span></button>
            </div>
        </div>
    </div>
    
    <!-- JS Core -->
    