from pywebcopy import save_website

kwargs = {'project_name': 'politicalresources.kg', 'over_write': True, 'bypass_robots': True, 'zip_project_folder': False,
          'debug': True, "join_timeout":5}

save_website(
    url='https://www.politicalresources.net/kyrgyzstan.htm',
    project_folder='C:/Users/valeriya.nikiforova/Documents/UCA\Senior/FYP/remote_library_static_server/governmental_resources',
    **kwargs
)
