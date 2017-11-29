# CKAN Embed

CKAN extension that allows organizations to embed their datasets published on a CKAN instance to their website within an iframe.

## How it works

You create an empty div on your website and attach a script that includes the url from CKAN with the required parameters to fetch the relevant datasets and display them on your website.

The iframe will include a search bar to help users search within the organization's datasets from the organization's website.

>**Note**: The extension uses [Pym.js](http://blog.apps.npr.org/pym.js/) for responsive embeds.

### Embedding

To fetch the datasets from an organization to be displayed on their website in a division, use the following code snippet:
```
  <div id="example"> </div> <!-- Where the iframe will be rendered -->

  <!-- At the end of the body --->
  <script type="text/javascript" src="https://pym.nprapps.org/pym.v1.min.js"></script>
  <script>
      var pymParent = new pym.Parent('example', 'https://<ckan-url>/embed/?organization=<organization-name>');
      pymParent.sendWidth();
  </script>

```

Example: For an organization called `org-x` the snippet would be:
```
  <div id="example"> </div> <!-- Where the iframe will be rendered -->

  <!-- At the end of the body --->
  <script type="text/javascript" src="https://pym.nprapps.org/pym.v1.min.js"></script>
  <script>
      var pymParent = new pym.Parent('example', 'https://<ckan-url>/embed/?organization=org-x');
      pymParent.sendWidth();
  </script>

```

## Installation

Install this extension in your CKAN instance is as easy as install any other CKAN extension.

* Activate your virtual environment
```
. /usr/lib/ckan/default/bin/activate
```
* Install the extension
```
pip install ckanext-embed
```
> **Note**: If you prefer, you can also download the source code and install the extension manually. To do so, execute the following commands:
> ```
> $ git clone https://github.com/CodeForAfricaLabs/ckanext-embed.git
> $ cd ckanext-embed
> $ python setup.py install
> ```

* Modify your configuration file (generally in `/etc/ckan/default/production.ini`) and add `embed` in the `ckan.plugins` property.
```
ckan.plugins = embed <OTHER_PLUGINS>
```
* Restart your apache2 reserver
```
sudo service apache2 restart
```
* That's All!

## Manual Testing

After the extension is successfully installed on a running CKAN instance:

* Create an organization and add public datasets to it

* Create an empty div with an id to be passed into the script as follows:
```
  <div id="example"> </div> <!-- Where the iframe will be rendered -->

  <!-- At the end of the body --->
  <script type="text/javascript" src="https://pym.nprapps.org/pym.v1.min.js"></script>
  <script>
      var pymParent = new pym.Parent('example', 'https://<ckan-url>/embed/?organization=<organization-name>');
      pymParent.sendWidth();
  </script>

```
>**Note**: The `<organization-name>` is the one that appears on the organization url

* If everything is set up successfully, the datasets you created should appear within the iframe as shown below and is should be responsive

### Screenshots

View of list of datasets:
![View of list of datasets:](https://user-images.githubusercontent.com/8082197/33073006-8e3f6704-ced2-11e7-960a-5b13af8365fe.png)

View of a single dataset's details:
![View of a single dataset's details](https://user-images.githubusercontent.com/8082197/33073022-986f1cec-ced2-11e7-9212-3318f697954e.png)


**Note:** When creating a PR that includes code changes, please, ensure your new code is tested. No PR will be merged until the Travis CI system marks it as valid.
