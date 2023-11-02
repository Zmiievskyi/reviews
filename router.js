const express = require("express");
const router = express.Router();
// const ctrl = require("./controller");


router.post("/data", (req, res) => {
    const jsonData = req.body;
  
    // You can now work with the JSON data (jsonData) as needed
    console.log('Received JSON data:', jsonData);
  
    // Send a response if needed
    res.status(200).json({ message: 'Data received successfully' });
  });

module.exports = router;
