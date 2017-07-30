class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []
        if not postData['f_name'] or len(postData['f_name']) < 2:
            results['status'] = False
            results['errors'].append('First name must be two characters or logner')
        if not postData['l_name'] or len(postData['l_name']) < 2:
            results['status'] = False
            results['errors'].append('Last name must be two characters or logner')
        if not postData['email'] or not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        postData['email']):
            results['status'] = False
            results['errors'].append('Email invalid. Please try again')
        if not postData['password'] or len(postData['password']) < 2 or postData['password'] != postdata['c_password']:
            results['status'] = False
            results['errors'].append('Last name must be two characters or logner')
        if results['status'] = True:
            user = User.objects.filter(email = postData['email'])
        if len(user) != 0:
            results['status'] = False
            results['errors'].append('Please try email again.')
        return results                
