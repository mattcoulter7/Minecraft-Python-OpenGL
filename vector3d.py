from math import sqrt,atan2
MIN_FLOAT = 1e-300


class Vector3D(object):
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z

    def zero(self):
        ''' set x and y and z to zero '''
        self.x = 0.
        self.y = 0.
        self.z = 0.

    def is_zero(self):
        ''' return true if both x and y and z are zero '''
        return self.magnitude_sq() < MIN_FLOAT

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magnitude_sq(self):
        ''' return the squared length (avoid sqrt()) '''
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def truncate(self, maxlength):
        ''' limit the length (scale x and y) to maxlength '''
        if self.length() > maxlength:
            self.normalise()  # unit vector length = 1.0
            self *= maxlength  # so length is 1.0 * maxlength

    def get_reverse(self):
        ''' return a new vector that is the reverse of self. '''
        return Vector3D(-self.x, -self.y, -self.z)

    def horizontal_angle_with(self,v2):
        return atan2(v2.z, v2.x) - atan2(self.z, self.x)
    def vertical_angle_with(self,v2):
        return atan2(v2.z, v2.y) - atan2(self.z, self.y)

    @property
    def list(self):
        return [self.x,self.y,self.z]

    def distance(self, v2):
        ''' the distance between self and v2 vector '''
        dx = v2.x - self.x
        dy = v2.y - self.y
        dz = v2.z - self.z
        return sqrt(dx*dx + dy*dy + dz*dz)

    def distance_sq(self, v2):
        ''' the squared distance between self and v2 vector '''
        dx = v2.x - self.x
        dy = v2.y - self.y
        dz = v2.z - self.z
        return dx*dx + dy*dy + dz*dz

    def dot(self, v2):
        return self.x*v2.x + self.y*v2.y + self.z*v2.z

    def normalise(self):
        ''' normalise self to a unit vector of length = 1.0 '''
        l = self.magnitude()
        try:
            self.x /= l
            self.y /= l
            self.y /= l
        except ZeroDivisionError:
            self.x = 0.
            self.y = 0.
            self.z = 0.
        return self

    def __neg__(self):  # -
        ''' get_reverse(), but using - operator based instead. '''
        return Vector3D(-self.x, -self.y, -self.z)

    def copy(self):
        ''' Simple copy Vector2D with self values '''
        return Vector3D(self.x, self.y, self.z)

    def round_to(self,rhs):
        return self - self % rhs

    def __iadd__(self, v2):  # +=
        self.x += v2.x
        self.y += v2.y
        self.z += v2.z
        return self

    def __isub__(self, v2):  # -=
        self.x -= v2.x
        self.y -= v2.y
        self.z -= v2.z
        return self

    def __imul__(self, rhs):  # *=
        self.x *= rhs
        self.y *= rhs
        self.z *= rhs
        return self

    def __itruediv__(self, rhs):  # /=
        self.x /= rhs
        self.y /= rhs
        self.z /= rhs
        return self

    def __eq__(self, v2):  # ==
        return is_equal(self.x, v2.x) and is_equal(self.y, v2.y) and is_equal(self.z, v2.z)

    def __ne__(self, v2):  # !=
        return (self.x != v2.x) or (self.y != v2.y) or (self.z != v2.z)

    def __add__(self, v2):  # self + v2
        return Vector3D(self.x+v2.x, self.y+v2.y, self.z+v2.z)

    def __sub__(self, v2):  # self - v2
        return Vector3D(self.x-v2.x, self.y-v2.y, self.z-v2.z)

    def __mod__(self, rhs):  # self % rhs
        return Vector3D(self.x%rhs, self.y%rhs, self.z%rhs)

    def __mul__(self, rhs):  # self * v2 (scalar)
        return Vector3D(self.x*rhs, self.y*rhs, self.z*rhs)

    def __rmul__(self, lhs):  # lhs (scalar) * self
        return Vector3D(self.x*lhs, self.y*lhs)

    def __truediv__(self, rhs):  # self / v2 (scalar)
        return Vector3D(self.x/rhs, self.y/rhs, self.z/rhs)

    def __rtruediv__(self, lhs):  # lhs (scalar) / self
        return Vector3D(lhs/self.x, lhs/self.y, lhs/self.z)

    def __str__(self):
        return '[%7.2f, %7.2f, %7.2f]' % (self.x, self.y, self.z)
