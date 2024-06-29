<script>
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
  
    export let columns = [];
    export let data = [];
    export let pageSize = 5;
  
    let sortedColumn = writable(null);
    let sortDirection = writable('asc');
    let currentPage = writable(1);
    let filteredData = writable(data);
  
    const sortData = (column) => {
      const isAscending = $sortedColumn === column && $sortDirection === 'asc';
      $sortDirection = isAscending ? 'desc' : 'asc';
      $sortedColumn = column;
      filteredData.update(data => {
        return [...data].sort((a, b) => {
          if (a[column] < b[column]) return $sortDirection === 'asc' ? -1 : 1;
          if (a[column] > b[column]) return $sortDirection === 'asc' ? 1 : -1;
          return 0;
        });
      });
    };
  
    const goToPage = (page) => {
      $currentPage = page;
    };
  
    $: paginatedData = $filteredData.slice(($currentPage - 1) * pageSize, $currentPage * pageSize);
  
    const handleEdit = (row) => {
      alert(`Edit ${row.name}`);
    };
  
    onMount(() => {
      filteredData.set(data);
    });
  </script>
  
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      padding: 8px;
      border: 1px solid #ddd;
    }
    th {
      cursor: pointer;
      background-color: #f2f2f2;
    }
    .pagination {
      margin: 20px 0;
      text-align: center;
    }
    .pagination button {
      margin: 0 2px;
      padding: 5px 10px;
      cursor: pointer;
    }
  </style>
  
  <table class="w-full min-w-[640px] table-auto">
    <thead>
      <tr>
        {#each columns as column}
          <th class="border-b border-blue-gray-50 py-3 px-6 text-left" on:click={() => sortData(column.field)}>
            <p class="block antialiased font-sans text-[11px] font-medium uppercase text-blue-gray-400">
              {column.header}
              {#if $sortedColumn === column.field}
                {#if $sortDirection === 'asc'} ▲ {/if}
                {#if $sortDirection === 'desc'} ▼ {/if}
              {/if}
            </p>
          </th>
        {/each}
        <th class="border-b border-blue-gray-50 py-3 px-6 text-left">
          <p class="block antialiased font-sans text-[11px] font-medium uppercase text-blue-gray-400">Actions</p>
        </th>
      </tr>
    </thead>
    <tbody>
      {#each paginatedData as row}
        <tr>
          {#each columns as column}
            <td class="py-3 px-5 border-b border-blue-gray-50">
              {#if column.field === 'completion'}
                <div class="w-10/12">
                  <p class="antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600">{row[column.field]}%</p>
                  <div class="flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1">
                    <div class="flex justify-center items-center h-full bg-gradient-to-tr {row[column.field] == 100 ? 'from-green-600 to-green-400' : 'from-blue-600 to-blue-400'} text-white" style="width: {row[column.field]}%;"></div>
                  </div>
                </div>
              {:else}
                <p class="block antialiased font-sans {column.field === 'name' ? 'text-sm leading-normal text-blue-gray-900 font-bold' : 'text-xs font-medium text-blue-gray-600'}">{row[column.field]}</p>
              {/if}
            </td>
          {/each}
          <td class="py-3 px-5 border-b border-blue-gray-50">
            <button class="text-blue-500 hover:text-blue-700" on:click={() => handleEdit(row)}>Edit</button>
          </td>
        </tr>
      {/each}
    </tbody>
  </table>
  
  <div class="pagination">
    {#each Array(Math.ceil($filteredData.length / pageSize)) as _, index}
      <button on:click={() => goToPage(index + 1)}>{index + 1}</button>
    {/each}
  </div>
  