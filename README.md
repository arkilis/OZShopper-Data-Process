## OZShopper 电商数据处理

### TODO:
* [ ] Cross listing
  * [ ] 能够 export 到 myDeal CSV
  * [ ] 能够 export 到 eBay
  * [ ] 能够 export 到 facebook marketplace
  * [ ] Google Merchant
* [ ] 生成销售报告，类似Apple的那种自动提醒销量
* [ ] 统计广告费用
* [ ] 备份数据
  * OZShopper的网站数据
  * 销售数据
  * 广告数据
* [ ] 数据分析
  * 能够分析每个产品的 ROI，这个可以多找一找小红书上面的`选品`帖子学习一下格式
* Optional: 每个商品有一个单独的二维码，录入的时候更新，卖出的时候自动更新系统


## 上货
OZShopper是整个数据的核心，供销存的枢纽
主要在 https://OZShopper.com.au 上面上货：
* Step 1: 使用 MS Edge 插件 下载图片
* Step 2: Woocommerce 里面 添加文字描述，改正格式和错别字。添加"
  * `my_deal_category_id`: https://docs.google.com/spreadsheets/d/1g_yEKSRfmA8J9jkElbdq_x4Db6lnvTBgjZE8AQL2rr4/edit?gid=36710004#gid=36710004
  * `search_keywords`: I am selling [makeup organisers], they have the following features, pls list the search keywords as many as possible, separated with comma:


## MyDeal importer 使用指南

