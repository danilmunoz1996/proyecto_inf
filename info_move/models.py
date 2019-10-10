from django.db import models
# Create your models here.

class ManejadorUsuario(BaseUserManager):
	def create_user(self, nombre_usuario, nombre_completo, correo, rut, password = None):
		if not rut:
			raise ValueError('debe ingresar un rut')
		if not correo:
			raise ValueError('debe ingresar un correo')
		if not nombre_usuario:
			raise ValueError('debe ingresar un nombre de usuario')
		if not nombre_completo:
			raise ValueError('debe ingresar su nombre completo')

		usuario = self.model(nombre_usuario = nombre_usuario, nombre_completo = nombre_completo, correo = correo, rut = rut)
		usuario.set_password(password)
		usuario.save(using = self._db)
		return usuario

	def create_staffuser(self, nombre_usuario, password):
		usuario = self.create_user(nombre_usuario = nombre_usuario, nombre_completo = nombre_usuario, correo = nombre_usuario + '@staff.cl', rut = nombre_usuario, password = password)
		usuario.staff = True
		usuario.save(using = self._db)
		return usuario

	def create_superuser(self, nombre_usuario, password):
		usuario = self.create_user(nombre_usuario = nombre_usuario, nombre_completo = nombre_usuario, correo = nombre_usuario + '@admin.cl', rut = nombre_usuario, password = password)
		usuario.staff = True
		usuario.admin = True
		usuario.save(using = self._db)
		return usuario

class Usuario(AbstractUser):
	correo = models.EmailField(max_length = 100, unique = True)
	nombre_usuario = models.CharField(max_length = 50, unique = True)
	nombre_completo = models.CharField(max_length = 100)
	rut = models.CharField(max_length = 30, unique = True, primary_key = True)
	staff = models.BooleanField(default = False)
	admin = models.BooleanField(default = False)

	USERNAME_FIELD = 'nombre_usuario'
	REQUIRED_FIELDS = []
	
	objects = ManejadorUsuario()

	class Meta:
		verbose_name = 'usuario'
		verbose_name_plural = 'usuarios'

	def __str__(self):
		return self.nombre_completo + ' ' + self.correo

	def has_perm(self, perm, obj = None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff
	
	@property
	def is_admin(self):
		return self.admin
	
class Empresa(models.Model):
	nombre = models.CharField(max_length = 100, unique = True, null = False)
	identificador = models.AutoField(unique = True, primary_key = True)

	class Meta:
		verbose_name = 'empresa'
		verbose_name_plural = 'empresas'

class Paradero(models.Model):
	x = models.DecimalField(max_digits = 30, decimal_places = 10, null = False)
	y = models.DecimalField(max_digits = 30, decimal_places = 10, null = False)
	identificador = models.AutoField(unique = True, primary_key = True)

	class Meta:
		verbose_name = 'paradero'
		verbose_name_plural = 'paraderos'

class Conductor(models.Model):
	nombre = models.CharField(max_length = 100, null = False)
	foto = models.CharField(max_length = 500, null = True)
	puntaje = models.DecimalField(max_digits = 3, decimal_places = 2, null = False)
	identificador = models.AutoField(unique = True, primary_key = True)

	class Meta:
		verbose_name = 'conductor'
		verbose_name_plural = 'conductores'

class Recorrido(models.Model):
	identificador = models.AutoField(unique = True, primary_key = True)
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)
	letra = models.CharField(max_length = 10, null = False)

	class Meta:
		verbose_name = 'recorrido'
		verbose_name_plural = 'recorridos'

class Valoracion(models.Model):
	puntaje = models.PositiveSmallIntegerField(null = False)
	comentario = models.CharField(max_length = 200, null = False)
	fecha = models.DateField(auto_now = False, auto_now_add = True)
	emisor = models.ForeignKey(Usuario, on_delete = models.CASCADE)
	receptor = models.ForeignKey(Conductor, on_delete = models.CASCADE)
	identificador = models.AutoField(unique = True, primary_key = True)

	class Meta:
		verbose_name = 'valoracion'
		verbose_name_plural = 'valoraciones'

class Micro(models.Model):
	patente = models.CharField(max_length = 10, primary_key = True, unique = True)
	recorrido = models.ForeignKey(Recorrido, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'micro'
		verbose_name_plural = 'micros'

class Itinerario(models.Model):
	inicio = models.PositiveSmallIntegerField(null = False)
	fin = models.PositiveSmallIntegerField(null = False)
	identificador = models.AutoField(unique = True, primary_key = True)
	micro = models.ForeignKey(Micro, on_delete = models.CASCADE)

	class Meta:
		verbose_name = 'itinerario'
		verbose_name_plural = 'itinerarios'

class PasaPor(models.Model):
	paradero = models.ForeignKey(Paradero, on_delete = models.CASCADE)
	micro = models.ForeignKey(Micro, on_delete = models.CASCADE)
	identificador = models.AutoField(unique = True, primary_key = True)

class Realiza(models.Model):
	micro = models.ForeignKey(Micro, on_delete = models.CASCADE)
	recorrido = models.ForeignKey(Recorrido, on_delete = models.CASCADE)

class Conduce(models.Model):
	identificador = models.AutoField(unique = True, primary_key = True)
	fecha = models.DateField(auto_now = False, auto_now_add = True)
	conductor = models.ForeignKey(Conductor, on_delete = models.CASCADE)
	itinerario = models.ForeignKey(Itinerario, on_delete = models.CASCADE)

