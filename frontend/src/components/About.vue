<template>
<div>
  <div>
    <h4> {{ msg }} </h4>
  </div>
  <div class="row">
    <div>
      <a v-bind:href="contact_details.facebook" target="_blank"><img class="img_position" src="../assets/facebook_icon.png" alt="Smiley face" height="24" width="24"></a>
    </div>
    <div>
      <a v-bind:href="contact_details.instagram" target="_blank"><img class="img_position_insta" src="../assets/instagram.png" alt="Smiley face" height="24" width="24"></a>
    </div>
  </div>
  <div><img v-bind:src="'https://upload.wikimedia.org/wikipedia/commons/8/84/' + poznan" width="200"/></div>
</div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'About',
  data() {
    return {
    msg: ".. a dress near you!",
    contact_details: null,
    loading: true,
    errored: false,
    poznan: 'Collage_of_views_of_Pozna%C5%84%2C_Poland.jpg'
    }
  },
  mounted() {
    const path = `http://localhost:5000/api/gummie/contacts`
    axios.get(path)
    .then(response => {
      this.contact_details = response.data
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(()=> this.loading = false)
  }
}
</script>


<style scoped>
  h4 {
  font-weight: normal;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: darkred;
  font-size: 18px;
}

.img_position {
  position: absolute;
  top: 50px;
  right: 20px;
}

.img_position_insta {
  position: absolute;
  top: 50px;
  right: 80px;
}

.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
