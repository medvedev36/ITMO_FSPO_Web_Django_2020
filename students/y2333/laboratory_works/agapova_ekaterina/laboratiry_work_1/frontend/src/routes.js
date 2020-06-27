import Store from "./Store";
import Login from "./Login";
import Register from "./Register";
import Profile from "./Profile";
import Admin from "./admin/Admin";
import Users from "./admin/Users";
import List from "./admin/List";
import Fabrics from "./admin/Fabrics";
import Products from "./admin/Products";
import Deliveries from "./admin/Deliveries";
import Sales from "./admin/Sales";

/**
 * Данные о всех маршрутах и их представлениях
 */
export default [
  {
    path: '/',
    component: Store
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/user',
    component: Profile
  },
  {
    path: '/adminpanel',
    component: Admin,
    children: [
      {
        path: '',
        component: List
      },
      {
        path: 'users',
        component: Users
      },
      {
        path: 'fabrics',
        component: Fabrics
      },
      {
        path: 'products',
        component: Products
      },
      {
        path: 'deliveries',
        component: Deliveries
      },
      {
        path: 'sales',
        component: Sales
      },
    ]
  }
];
