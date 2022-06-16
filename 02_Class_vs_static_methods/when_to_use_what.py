'''
When to use class methods and when to use static methods
'''

class Item:
    @staticmethod
    def not_unique_per_instance():
        '''
        We use a static method when we have to do something that's not unique per instance. It can literally be used a seperate isolated function that's why its called a 'static' method. 
        It does not take the object as its first argument like the normal instances do.
        '''

    @classmethod
    def instantiating_from_data(cls):
        '''
        We use class methods for instantiating instances from some structured data we own already. 
        They are used to manipulate different structures of data to instantiate objects, like we did with CSV. 
        The class object itself is passed as a first, default argument in the background
        '''