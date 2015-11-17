from django.core.urlresolvers import reverse_lazy
from post.forms import PostForm
from post.models import Location, Category, SubCategory, Post
from django.views.generic import ListView, CreateView


class LocationList(ListView):
    model = Location
    template_name = "post/location_list.html"
    queryset = Location.objects.all().order_by('state')


class CategoryList(ListView):
    model = Category
    template_name = "post/category.html"
    queryset = Category.objects.all().order_by('title')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = SubCategory.objects.all()
        return context


class CreatePost(CreateView):
    model = Post
    from_class = PostForm
    success_url = reverse_lazy('location_list')
    template_name = 'post/posting.html'
    fields = ['title', 'description', 'user_email', 'phone_number', 'zipcode', 'images', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)





# class SubCategoryList(ListView):
#     model = SubCategory
#     template_name = "post/category.html"
#     queryset = SubCategory.objects.all().order_by('title')
