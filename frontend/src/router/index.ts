import { createRouter, createWebHistory } from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import {isAuthenticated} from "@/lib/auth.ts";
import LoggedLayout from "@/layouts/LoggedLayout.vue";
import CreateAdCampaignView from "@/views/CreateAdCampaignView.vue";
import EditAdCampaignView from "@/views/EditAdCampaignView.vue";

const routes = [
  {
    path: '/',
    name: 'home',
    component: LoggedLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        name: 'Home',
        component: HomeView,
      },
      {
        path: '/adCampaigns/create',
        name: 'CreateAdCampaign',
        component: CreateAdCampaignView
      },
      {
        path: '/adCampaigns/:id',
        name: 'AdCampaign',
        component: EditAdCampaignView
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'register',
    component: SignupView
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  const authRequired = to.matched.some((record) => record.meta.requiresAuth)
  const loggedIn = isAuthenticated()

  if (authRequired && !loggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router
