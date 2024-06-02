<script>
  import Cart from "$lib/components/UI/Cart.svelte";
import Header from "$lib/components/UI/Header.svelte";
  import MenuItem from "$lib/components/UI/MenuItem.svelte";
  import Modal from "$lib/components/UI/Modal.svelte";
</script>

<svelte:head>
    <link rel="stylesheet" type="text/css" href=http://localhost:5177/core.css/>
    <!-- CSS Theme -->
    <link id="theme" rel="stylesheet" href="http://localhost:5177/css/theme-beige.css" />
</svelte:head>


    <!-- Body Wrapper -->
    <div id="body-wrapper" class="animsition">
    
        
        <Header></Header>
    
        
    
        <!-- Content -->
        <div id="content">
    
            <!-- Page Title -->
            <div class="page-title bg-light">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 offset-lg-4">
                            <h1 class="mb-0">Menu List</h1>
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
                            <div id="Burgers" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuBurgersContent" data-toggle="collapse" aria-expanded="true">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-burgers.jpg" alt=""></div>
                                    <h2 class="title">Burgers</h2>
                                </div>
                                <div id="menuBurgersContent" class="menu-category-content collapse show">
                                    <MenuItem></MenuItem>
                                    <MenuItem></MenuItem>
                                    
                                    
                                </div>
                            </div>
                            <!-- Menu Category / Pasta -->
                            <div id="Pasta" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuPastaContent" data-toggle="collapse" aria-expanded="false">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-pasta.jpg" alt=""></div>
                                    <h2 class="title">Pasta</h2>
                                </div>
                                <div id="menuPastaContent" class="menu-category-content collapse">
                                    <MenuItem></MenuItem>
                                    
                                    
                                </div>
                            </div>
                            <!-- Menu Category / Pizza -->
                            <div id="Pizza" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuPizzaContent" data-toggle="collapse" aria-expanded="false">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-pizza.jpg" alt=""></div>
                                    <h2 class="title">Pizza</h2>
                                </div>
                                <div id="menuPizzaContent" class="menu-category-content collapse">
                                    
                                    <MenuItem></MenuItem>
                                    
                                    
                                </div>
                            </div>
                            <!-- Menu Category / Sushi -->
                            <div id="Sushi" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuSushiContent" data-toggle="collapse" aria-expanded="false">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-sushi.jpg" alt=""></div>
                                    <h2 class="title">Sushi</h2>
                                </div>
                                <div id="menuSushiContent" class="menu-category-content collapse">
                                    <MenuItem></MenuItem>
                                    
                                    
                                </div>
                            </div>
                            <!-- Menu Category / Desserts -->
                            <div id="Desserts" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuDessertsContent" data-toggle="collapse" aria-expanded="false">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-desserts.jpg" alt=""></div>
                                    <h2 class="title">Desserts</h2>
                                </div>
                                <div id="menuDessertsContent" class="menu-category-content collapse">
                                    
                                    <MenuItem></MenuItem>
                                </div>
                            </div>
                            <!-- Menu Category / Drinks -->
                            <div id="Drinks" class="menu-category">
                                <div class="menu-category-title collapse-toggle" role="tab" data-target="#menuDrinksContent" data-toggle="collapse" aria-expanded="false">
                                    <div class="bg-image"><img src="http://assets.suelo.pl/soup/img/photos/menu-title-drinks.jpg" alt=""></div>
                                    <h2 class="title">Drinks</h2>
                                </div>
                                <div id="menuDrinksContent" class="menu-category-content collapse">
                                    <MenuItem></MenuItem>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
    
        </div>
        <!-- Content / End -->
    
        
        <Cart></Cart>
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
    
    <Modal></Modal>
    
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
    