# CKAN Embed

CKAN extension that allows organizations to embed their datasets published on a CKAN instance to their website within an iframe.

## How it works

You create an iframe on your website and provide the url from CKAN with the required parameters to fetch the relevant datasets and display them on your website.

The iframe will include a search bar to help users search within the organization's datasets from the organization's website.

### Embedding

To fetch the datasets from an organization to be displayed on their website in an iframe, use the following code snippet:
```
<iframe
  width="600"
  height="450"
  frameborder="0" style="border:0"
  src="https://<ckan-url>/embed/?organization=<organization-id>" >
</iframe>
```

Example: For an organization called `org-x` the snippet would be:
```
<iframe
  width="600"
  height="450"
  frameborder="0" style="border:0"
  src="https://<ckan-url>/embed/?organization=org-x">
</iframe>
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

**Note:** When creating a PR that includes code changes, please, ensure your new code is tested. No PR will be merged until the Travis CI system marks it as valid.
