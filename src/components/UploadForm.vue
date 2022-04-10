<template>
<div class="form_container">
        <form @submit.prevent="uploadPhoto" id="uploadForm">

            <label for="description">Description</label>
            <div class="form-floating">
              <input type="text" id="description" name="description">
            </div>

            <label for="photo">Photo</label>
            <div class="form-floating">
              <input type="file" id="Image" name="Image">
            </div>

            <input type="submit" value="Submit">
          </form>
</div>
</template>

<script>
let uploadForm = document.getElementById('uploadForm');
let form_data = new FormData(uploadForm);
 
uploadPhoto() {
 let uploadForm =
document.getElementById('uploadForm');
 let form_data = new FormData(uploadForm);
 fetch("/api/uploads", {
 method: 'POST',
 body: form_data,
 headers: {
 'X-CSRFToken': this.csrf_token
 }
 })
 .then(function (response) {
 return response.json();
 })
 .then(function (data) {
 // display a success message
 console.log(data);
 })
 .catch(function (error) {
 console.log(error);
 });
},

data() {
    return {
    csrf_token: ''
    }
},

created() {
 this.getCsrfToken();
},

getCsrfToken() {
    let self = this;
    fetch('/api/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    console.log(data);
    self.csrf_token = data.csrf_token;
    })
}
</script>