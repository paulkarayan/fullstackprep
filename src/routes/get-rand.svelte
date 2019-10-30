<script>
  import Slider from "components/Slider";
  let value = 5;

  let rand = -1;
  function getRand() {
    fetch("http://localhost:5000/rand")
      .then(response => {
        return response.json()
      })
      .then(data => {
        // Work with JSON data here
        console.log(data['data'])
        rand = data['data']
      })
      .catch(err => {
        // Do something for an error here
    })
  }

</script>

<h4>Your number is {rand}!</h4>


<div class="container max-w-xl items-center flex flex-col">
  
  <button on:click={getRand}>Get a random number</button>

</div>
