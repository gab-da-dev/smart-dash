<script>
    import {
        getRequest,
    } from "$lib/services/http_service";
    
  
    import DataTable from '../../../../lib/components/UI/DataTable.svelte';

  const columns = [
    { header: 'Name', field: 'name' },
    { header: 'active', field: 'active' },
  ];

  const data = [
  ];

  let product = {
        name: 'test',
        active: true,
        description: 'test',
        image: null,
        product_category_id: 'aaa0f3d1-339b-4a2d-acaa-092210823135',
        price: 2.3,
        prep_time: 5,
        ingredients: []
    }

 
</script>


{#await getRequest('product-category/all') then value}
    <DataTable {columns} data={value.items} pageSize={5}  create_url={'product-category/create'}
    edit_link={"categories"}/>
{/await}
<div class="p-6 overflow-x-scroll px-0 pt-0 pb-2">
  </div>