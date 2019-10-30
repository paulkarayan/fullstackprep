<script>
  import Slider from "components/Slider";
  
  let heads = 0 
  let tails = 0 

  let val = 5

  function getFlip() {
    console.log(val, "<----")
    fetch("http://localhost:5000/coinflips/"+val)
      .then(response => {
        return response.json()
      })
      .then(data => {
        // Work with JSON data here
        console.log(data['heads'], data['tails'])
        $: heads = data['heads']
        $: tails = data['tails']
      })
      .catch(err => {
        // Do something for an error here
    })
  }

</script>


<div class="container max-w-xl items-center flex flex-col">
  Heads {heads}
  Tails {tails}
  <h4 class="my-8">Coin Flip Simulator</h4>
  <caption>Number of coin flips: {val}</caption>
  <Slider min="1" max="100" bind:value={val} on:change={getFlip} />
  
  <!-- <caption>Number of coin flips:</caption>
  <input type=int bind:value={val}>
  <button on:click={getFlip}>Submit</button> -->


</div>
