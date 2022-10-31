# NFT-search_with_Flask_With_Autorization

##### A web application written in python and flask to search for NFT images by their address. It saves all NFTs in postgresql database.    

* ___P.S. I have set the default settings for postgres. If you have different    settings, open the base.py file in any text editor and change the settings to your own.___
***
## Installation

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

## Usage

* After deploying the web application, you need to write the address in the search bar on your browser. But firstly you need to go /register directory and register your login. After in /login directory, you can log in. 

If you want to logout, write /logout.

```
http://127.0.0.1:5000/
```
* After that, you will see a input-form on the web page, you need to enter the nft address there.

* Click submit and you redirect to new page

* If you entered everything correctly, you will receive the name, address and a link to information about nft.

___P.S. Sometimes, if an error pops up, you need to refresh the page___

***

# Examle

Submit ```3HcD2Zz7cpZShUbS4KTEAXfLu31Yb9zb8wcJmNB6cQsh``` addres to input form

Your ouput will be:
```
Rifter #2769

3HcD2Zz7cpZShUbS4KTEAXfLu31Yb9zb8wcJmNB6cQsh

https://arweave.net/Y9uF_M0QSitAGa9uRt6yZqLSrW3QEfi0x60FxdIPQjY/2769.json

 ```
<img src="https://sun9-35.userapi.com/impg/tshnK6_9mE4HUIN4kJBipBFHA4WaXhbxHKtgCg/ji6Hvxx9wu4.jpg?size=1870x961&quality=96&sign=55b1546dfff2bf822b8b58ec5c98be0c&type=album">

<img src="https://sun9-46.userapi.com/impg/shc2dY_E0Yk1xeo3934iNmbQUuhrYnox6TC6Ag/4eG3oJX6TxI.jpg?size=1869x960&quality=96&sign=48df29d1be4f2f9019a37ec0c449cbe3&type=album">

<img src="https://sun9-52.userapi.com/impg/ehRDAZjwfi2NLriEezZv7xu4LrPVyIg3yAHVBw/8IThykxc56Q.jpg?size=1870x963&quality=96&sign=efbc396b3c8633f225ccebe35f01ba75&type=album">
