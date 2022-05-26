import datetime
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.functional import cached_property
from django.http import Http404
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)

from wagtail.core.models import Page,Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField, RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField


from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting





# pagina de inicio
class consultas(AbstractFormField):
    page = ParentalKey('home', on_delete=models.CASCADE, related_name='form_fields')

class home(AbstractEmailForm):

    web_title = RichTextField(blank=True,verbose_name='Titulo de la pagina')

    # Empieza Banner de Slides
    banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
    banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
    banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
    banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
    banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
    banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')
    banner_title4 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
    banner_info4 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')


    # Empieza Banner de informacion de Servicios
    service_title = RichTextField(blank=True,verbose_name='Titulo de servicio-1')
    service_info = RichTextField(blank=True,verbose_name='Información de servicio-1')
    service_title2 = RichTextField(blank=True,verbose_name='Titulo de servicio-2')
    service_info2 = RichTextField(blank=True,verbose_name='Información de servicio-2')
    service_title3 = RichTextField(blank=True,verbose_name='Titulo de servicio-3')
    service_info3 = RichTextField(blank=True,verbose_name='Información de servicio-3')
    service_title4 = RichTextField(blank=True,verbose_name='Titulo de servicio-4')
    service_info4 = RichTextField(blank=True,verbose_name='Información de servicio-4')
    service_title5 = RichTextField(blank=True,verbose_name='Titulo de servicio-5')
    service_info5 = RichTextField(blank=True,verbose_name='Información de servicio-5')
    service_title6 = RichTextField(blank=True,verbose_name='Titulo de servicio-6')
    service_info6 = RichTextField(blank=True,verbose_name='Información de servicio-6')

    # Empieza Banner de informacion de Porfolio

    porfolio_title = RichTextField(blank=True,verbose_name='Titulo de porfolio')
    porfolio_info = RichTextField(blank=True,verbose_name='Información de porfolio')
    cartegory = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-1')
    cartegory2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-2')
    cartegory3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-3')
    cartegory4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-4')
    cartegory5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-5')
    cartegory6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de Categoria-6')

    descript = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-1')
    descript2 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-2')
    descript3 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-3')
    descript4 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-4')
    descript5 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-5')
    descript6 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-6')
    descript7 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-7')
    descript8 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-8')
    descript9 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-9')
    descript10 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-10')
    descript11 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-11')
    descript12 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-12')
    descript13 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-13')
    descript14 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-14')
    descript15 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-15')
    descript16 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-16')
    descript17 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-17')
    descript18 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-18')
    descript19 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-19')
    descript20 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-20')
    descript21 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-21')
    descript22 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-22')
    descript23 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-23')
    descript24 = models.CharField(max_length=500, null=True, blank=True,verbose_name='Descripción de Proyecto-24')

    # Empieza seccion de planes y costos

    plans_title = RichTextField(blank=True,verbose_name='Titulo de porfolio')
    plans_info = RichTextField(blank=True,verbose_name='Información de porfolio')

    # Empieza seccion de planes y costos

    plan_name = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de plan')
    plan_price = models.DecimalField(max_digits=100, decimal_places=2,null=True, blank=True,verbose_name='Precio del plan')
    plan_info = models.CharField(max_length=150, null=True, blank=True,verbose_name='info1 de plan')
    plan_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info2 de plan')
    plan_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info3 de plan')
    plan_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info4 de plan')
    plan_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info5 de plan')

    plan2_name = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de plan-2')
    plan2_price = models.DecimalField(max_digits=100, decimal_places=2,null=True, blank=True,verbose_name='Precio del plan-2')
    plan2_info = models.CharField(max_length=150, null=True, blank=True,verbose_name='info1 de plan-2')
    plan2_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info2 de plan-2')
    plan2_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info3 de plan-2')
    plan2_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info4 de plan-2')
    plan2_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info5 de plan-2')

    plan3_name = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de plan-3')
    plan3_price = models.DecimalField(max_digits=100, decimal_places=2,null=True, blank=True,verbose_name='Precio del plan-3')
    plan3_info = models.CharField(max_length=150, null=True, blank=True,verbose_name='info1 de plan-3')
    plan3_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info2 de plan-3')
    plan3_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info3 de plan-3')
    plan3_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info4 de plan-3')
    plan3_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info5 de plan-3')

    # Empieza seccion de Crew and Team

    team_title = RichTextField(blank=True,verbose_name='Titulo de Equipo')
    team_info = RichTextField(blank=True,verbose_name='Información de Equipo')

    crew_name = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo')
    crew_title = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo')
    crew_name2 = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo-2')
    crew_title2 = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo-2')
    crew_name3 = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo-3')
    crew_title3 = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo-3')
    crew_name4 = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo-4')
    crew_title4 = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo-4')
    crew_name5 = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo-5')
    crew_title5 = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo-5')
    crew_name6 = RichTextField(blank=True,verbose_name='Nombre del Ejecutivo-6')
    crew_title6 = RichTextField(blank=True,verbose_name='Cargo del Ejecutivo-6')

    # Empieza seccion direccion y telefono
    contact_title = RichTextField(blank=True,verbose_name='contact_title ')
    contact_info = RichTextField(blank=True,verbose_name='contact_info ')
    company_name = RichTextField(blank=True,verbose_name='company_name ')
    direccion = RichTextField(blank=True,verbose_name='Dirección')
    ciudad = RichTextField(blank=True,verbose_name='Dirección')
    numeracion = models.CharField(max_length=5, null=True, blank=True,verbose_name='Numeracion')
    telefono = models.CharField(max_length=5, null=True, blank=True,verbose_name='telefono')

    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [

        FieldPanel('web_title', classname="full"),

        # Empieza Banner de Slides

        FieldPanel('banner_title1', classname="full"),
        FieldPanel('banner_info1', classname="full"),
        FieldPanel('banner_title2', classname="full"),
        FieldPanel('banner_info2', classname="full"),
        FieldPanel('banner_title3', classname="full"),
        FieldPanel('banner_info3', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('banner_info4', classname="full"),

        # Empieza Banner de informacion de Servicios

        FieldPanel('service_title', classname="full"),
        FieldPanel('service_info', classname="full"),
        FieldPanel('service_title2', classname="full"),
        FieldPanel('service_info2', classname="full"),
        FieldPanel('service_title3', classname="full"),
        FieldPanel('service_info3', classname="full"),
        FieldPanel('service_title4', classname="full"),
        FieldPanel('service_info4', classname="full"),
        FieldPanel('service_title5', classname="full"),
        FieldPanel('service_info5', classname="full"),
        FieldPanel('service_title6', classname="full"),
        FieldPanel('service_info6', classname="full"),

        # Empieza Banner de informacion de Porfolio

        FieldPanel('porfolio_title', classname="full"),
        FieldPanel('porfolio_info', classname="full"),
        FieldPanel('cartegory', classname="full"),
        FieldPanel('cartegory2', classname="full"),
        FieldPanel('cartegory3', classname="full"),
        FieldPanel('cartegory4', classname="full"),
        FieldPanel('cartegory5', classname="full"),
        FieldPanel('cartegory6', classname="full"),
        FieldPanel('descript', classname="full"),
        FieldPanel('descript2', classname="full"),
        FieldPanel('descript3', classname="full"),
        FieldPanel('descript4', classname="full"),
        FieldPanel('descript5', classname="full"),
        FieldPanel('descript6', classname="full"),
        FieldPanel('descript7', classname="full"),
        FieldPanel('descript8', classname="full"),
        FieldPanel('descript9', classname="full"),
        FieldPanel('descript10', classname="full"),
        FieldPanel('descript11', classname="full"),
        FieldPanel('descript12', classname="full"),
        FieldPanel('descript13', classname="full"),
        FieldPanel('descript14', classname="full"),
        FieldPanel('descript15', classname="full"),
        FieldPanel('descript16', classname="full"),
        FieldPanel('descript17', classname="full"),
        FieldPanel('descript18', classname="full"),
        FieldPanel('descript19', classname="full"),
        FieldPanel('descript20', classname="full"),
        FieldPanel('descript21', classname="full"),
        FieldPanel('descript22', classname="full"),
        FieldPanel('descript23', classname="full"),
        FieldPanel('descript24', classname="full"),

        # Empieza seccion de planes y costos

        FieldPanel('plans_title', classname="full"),
        FieldPanel('plans_info', classname="full"),

        FieldPanel('plan_name', classname="full"),
        FieldPanel('plan_price', classname="full"),
        FieldPanel('plan_info', classname="full"),
        FieldPanel('plan_info2', classname="full"),
        FieldPanel('plan_info3', classname="full"),
        FieldPanel('plan_info4', classname="full"),
        FieldPanel('plan_info5', classname="full"),

        FieldPanel('plan2_name', classname="full"),
        FieldPanel('plan2_price', classname="full"),
        FieldPanel('plan2_info', classname="full"),
        FieldPanel('plan2_info2', classname="full"),
        FieldPanel('plan2_info3', classname="full"),
        FieldPanel('plan2_info4', classname="full"),
        FieldPanel('plan2_info5', classname="full"),

        FieldPanel('plan3_name', classname="full"),
        FieldPanel('plan3_price', classname="full"),
        FieldPanel('plan3_info', classname="full"),
        FieldPanel('plan3_info2', classname="full"),
        FieldPanel('plan3_info3', classname="full"),
        FieldPanel('plan3_info4', classname="full"),
        FieldPanel('plan3_info5', classname="full"),

        # Empieza seccion de Crew and Team
        FieldPanel('team_title', classname="full"),
        FieldPanel('team_info', classname="full"),
        FieldPanel('crew_name', classname="full"),
        FieldPanel('crew_title', classname="full"),
        FieldPanel('crew_name2', classname="full"),
        FieldPanel('crew_title2', classname="full"),
        FieldPanel('crew_name3', classname="full"),
        FieldPanel('crew_title3', classname="full"),
        FieldPanel('crew_name4', classname="full"),
        FieldPanel('crew_title4', classname="full"),
        FieldPanel('crew_name5', classname="full"),
        FieldPanel('crew_title5', classname="full"),
        FieldPanel('crew_name6', classname="full"),
        FieldPanel('crew_title6', classname="full"),

        #Empieza cntactos
        FieldPanel('contact_title', classname="full"),
        FieldPanel('contact_info', classname="full"),
        FieldPanel('company_name', classname="full"),
        FieldPanel('direccion', classname="full"),
        FieldPanel('ciudad', classname="full"),
        FieldPanel('numeracion', classname="full"),
        FieldPanel('telefono', classname="full"),

        #panel para campos de consulta
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria', label="Imagen de Fondo Barner"),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
    ]


class GaleriadeImagenes(Orderable):
    page = ParentalKey(home, on_delete=models.CASCADE, related_name='galleria')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo de la empresa')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-1')
    image1 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-1')
    image2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-1')
    image3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-1')

    image4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-2')
    image5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-2')
    image6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-2')
    image7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-2')

    image8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-3')
    image9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-3')
    image10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-3')
    image11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-3')

    image12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-4')
    image13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-4')
    image14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-4')
    image15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-4')

    image16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-5')
    image17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-5')
    image18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-5')
    image19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-5')

    image20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto-categoria-6')
    image21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto2-categoria-6')
    image22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto3-categoria-6')
    image23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='foto4-categoria-6')

    image24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile1')
    image25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile2')
    image26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile3')
    image27 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile4')
    image28 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile5')
    image29 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='profile6')




    panels = [
        ImageChooserPanel('logo'),
        ImageChooserPanel('image'),
        ImageChooserPanel('image2'),
        ImageChooserPanel('image3'),
        ImageChooserPanel('image4'),
        ImageChooserPanel('image5'),
        ImageChooserPanel('image6'),
        ImageChooserPanel('image7'),
        ImageChooserPanel('image8'),
        ImageChooserPanel('image9'),
        ImageChooserPanel('image10'),
        ImageChooserPanel('image11'),
        ImageChooserPanel('image12'),
        ImageChooserPanel('image13'),
        ImageChooserPanel('image14'),
        ImageChooserPanel('image15'),
        ImageChooserPanel('image16'),
        ImageChooserPanel('image17'),
        ImageChooserPanel('image18'),
        ImageChooserPanel('image19'),
        ImageChooserPanel('image20'),
        ImageChooserPanel('image21'),
        ImageChooserPanel('image22'),
        ImageChooserPanel('image23'),
        ImageChooserPanel('image24'),
        ImageChooserPanel('image25'),
        ImageChooserPanel('image26'),
        ImageChooserPanel('image27'),
        ImageChooserPanel('image28'),
        ImageChooserPanel('image29'),
    ]

@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True,null=True,help_text="")
    twitter = models.URLField(blank=True,null=True,help_text="")
    instagram = models.URLField(blank=True,null=True,help_text="")
    youtube = models.URLField(blank=True,null=True,help_text="")
    pinterest = models.URLField(blank=True,null=True,help_text="")
    google_plus = models.URLField(blank=True,null=True,help_text="")

    panels = [
        MultiFieldPanel(
            [
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("youtube"),
            FieldPanel("pinterest"),
            FieldPanel("google_plus"),
            ]
        ,heading= "Social Media Settings")
    ]
