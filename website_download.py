from pywebcopy import save_website

kwargs = {'project_name': 'president.kg', 'over_write': True, 'bypass_robots': True, 'zip_project_folder': False}

save_website(
    url='http://www.president.kg/kg/',
    project_folder='C:/Users/valeriya.nikiforova/Documents/UCA/Senior/FYP/remote_library_web/remote-library/public/projectMaterials/governmental_resources',
    **kwargs
)