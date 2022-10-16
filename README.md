# NFT-search_with_Flask

##### A web application written in python and flask to search for NFT images by their address. It saves all NFTs in postgresql database.    

* ___P.S. I have set the default settings for postgres. If you have different    settings, open the base.py file in any text editor and change the settings to your own.___
***
##Installation

* Clone the repository to your computer

```
git clone https://github.com/CogitoErgoSum12/NFT-search_with_Flask.git
```


* Go to folder with base.py file

```
cd NFT-search_with_Flask/src
```
* Run base.py to deploy web-application

```
python3 base.py
```

***

##Usage

* After deploying the web application, you need to write the address in the search bar on your browser

```
http://127.0.0.1:5000/
```
* After that, you will see a input-form on the web page, you need to enter the nft address there.

* Click submit and you redirect to new page

* If you entered everything correctly, you will receive the name, address and a link to information about nft.

___P.S. Sometimes, if an error pops up, you need to refresh the page___

***

#Examle

Submit ```3HcD2Zz7cpZShUbS4KTEAXfLu31Yb9zb8wcJmNB6cQsh``` addres to input form

Your ouput will be:
```
Rifter #2769

3HcD2Zz7cpZShUbS4KTEAXfLu31Yb9zb8wcJmNB6cQsh

https://arweave.net/Y9uF_M0QSitAGa9uRt6yZqLSrW3QEfi0x60FxdIPQjY/2769.json

 ```
