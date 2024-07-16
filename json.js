const fs = require('fs');
const axios = require('axios');

const urlJson = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/data.json';
const urlGoldValue = 'https://raw.githubusercontent.com/xiaoji235/py-jump/main/gold_value.txt';

const githubToken = process.env.GITHUB_TOKEN; // GitHub Personal Access Token

axios.get(urlJson)
  .then(response => {
    let data = response.data;

    axios.get(urlGoldValue)
      .then(response => {
        let goldValue = response.data.trim();

        data.gold = goldValue;

        fs.writeFileSync('new_data.json', JSON.stringify(data, null, 4));

        // 将新的 JSON 数据提交回 GitHub 仓库
        axios.put(urlJson, {
          message: 'Update gold value',
          content: fs.readFileSync('new_data.json', 'base64')
        }, {
          headers: {
            Authorization: `token ${githubToken}`,
            Accept: 'application/vnd.github.v3+json'
          }
        })
        .then(() => {
          console.log('Gold value has been updated in the GitHub repository.');
        })
        .catch(error => {
          console.error('Error updating JSON in the GitHub repository:', error.message);
        });

      })
      .catch(error => {
        console.error('Error fetching gold value:', error.message);
      });

  })
  .catch(error => {
    console.error('Error fetching JSON data:', error.message);
  });
