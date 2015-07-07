__author__ = 'Evren Esat Ozkan'
from pyoko.form import ModelForm, Form

class AngularForm(Form):
    def serialize(self):
        result = {
            "schema": {
                "title": self.title,
                "type": "object",
                "properties": {},
                "required": []
            },
            "form": [],
            "model": {}
        }
        for itm in self._serialize():
            result["schema"]["properties"][itm['name']] = {'type': itm['type'],
                                                           'title': itm['title']}
            result["model"][itm['name']] = itm['value'] or itm['default']
            result["form"].append(itm['name'])
            if itm['required']:
                result["schema"]["required"].append(itm['name'])
        return result


