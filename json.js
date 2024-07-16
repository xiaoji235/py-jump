const fs = require('fs');
const axios = require('axios');

const urlJson = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/data.json';
const urlGoldValue = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/gold_value.txt';

axios.get(urlJson)
  .then(response => {
    let data = response.data;

    axios.get(urlGoldValue)
      .then(response => {
        let goldValue = response.data.trim();

        data.gold = goldValue;

        fs.writeFile('new_data.json', JSON.stringify(data, null, 4), (err) => {
          if (err) throw err;
          console.log('Gold value has been updated in new_data.json.');
        });
      })
      .catch(error => {
        console.error('Error fetching gold value:', error.message);
      });

  })
  .catch(error => {
    console.error('Error fetching JSON data:', error.message);
  });
