from lxml import etree

tree = etree.parse('demo/xpath/test.html')
title_tag = tree.xpath('/html/head/title')
  
title_tag = tree.xpath('//title')

div_tags = tree.xpath('//div')

div_tag = tree.xpath('//div[@class="song"]')
div_tag = tree.xpath('//div[1]')

a_list = tree.xpath('//div[@class="tang"]/ul/li/a')
a_list = tree.xpath('//div[@class="tang"]//a')

a_content = tree.xpath('//a[@id="feng"]/text()')[0]
div_content = tree.xpath('//div[@class="song"]//text()')

img_src = tree.xpath('//img/@src')[0]
print(img_src)