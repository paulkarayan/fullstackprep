<script>
  import { stores } from "@sapper/app";
  import { onMount } from "svelte";
  import { fade } from "svelte/transition";

  import AppBar from "components/AppBar";
  import Tabs from "components/Tabs";
  import Button from "components/Button";
  import { Spacer } from "components/Util";
  import List from "components/List";
  import ListItem from "components/List/ListItem.svelte";
  import NavigationDrawer from "components/NavigationDrawer";
  import ProgressLinear from "components/ProgressLinear";

  import {
    right,
    elevation,
    persistent,
    showNav,
    showNavMobile,
    breakpoint
  } from "smelte/src/stores.js";

  const { preloading, page } = stores();

  let selected = "";
  const bp = breakpoint();
  $: path = $page.path;

  const projects = [
                       { to: "/get-rand", text: "Get Random Integer (easy flask)" },
                       { to: "/coinflip", text: "Coin Flip" }
                  ];

  const tophighlights = [
    { to: "/about", text: "About" },
    { to: "/highlights", text: "Highlights" }
  ];
</script>

{#each projects as link}
  <a href={link.to} class="hidden">{link.text}</a>
{/each}

<svelte:head>
  <title>Paul's Full Stack Prep Shack</title>
</svelte:head>

{#if $preloading}
  <ProgressLinear app />
{/if}

<AppBar>
  <a href="." class="px-2 md:px-8 flex items-center">
    <img src="/logo.png" alt="Smelte logo" width="44" />
    <h6 class="pl-3 text-white tracking-widest font-thin text-lg">Paul's Full Stack Prep Shack</h6>
  </a>
  <Spacer />
  <Tabs navigation items={tophighlights} bind:selected={path} />
  <div class="md:hidden">
    <Button
      icon="highlights"
      small
      flat
      add="text-white"
      remove="p-1 h-4 w-4"
      iconClasses={i => i.replace('p-4', 'p-3').replace('m-4', 'm-3')}
      text
      on:click={() => showNavMobile.set(!$showNavMobile)} />
  </div>
</AppBar>

{#if $bp}
  <main
    class="container relative p-8 lg:max-w-3xl lg:ml-64 mx-auto mb-10 mt-24
    md:ml-56 md:max-w-md md:px-3"
    transition:fade={{ duration: 300 }}>
    <NavigationDrawer
      bind:showDesktop={$showNav}
      bind:showMobile={$showNavMobile}
      right={$right}
      persistent={$persistent}
      elevation={$elevation}
      breakpoint={$bp}>
      <h6 class="p-6 ml-1 pb-2 text-xs text-gray-900"> </h6>
      <hr>
      <List items={tophighlights}>
        <span slot="item" let:item class="cursor-pointer">
          <a href={item.to}>
            <ListItem
              selected={path.includes(item.to)}
              {...item}
              dense
              navigation />
          </a>
        </span>
      </List>
      
      <hr>

      <List items={projects}>
        <span slot="item" let:item class="cursor-pointer">
          <a href={item.to}>
            <ListItem
              selected={path.includes(item.to)}
              {...item}
              dense
              navigation />
          </a>
        </span>
      </List>
      <hr />
    </NavigationDrawer>

    <slot />
  </main>
{/if}
