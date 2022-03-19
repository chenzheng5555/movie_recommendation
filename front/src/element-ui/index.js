
import Vue from 'vue'
import {
  Form,
  FormItem,
  Input,
  Button,
  Row,
  Col,
  Link,
  Message,
  MessageBox,
  Loading,
  Tabs,
  TabPane,
  Card,
  Dialog,
  Menu,
  Submenu,
  MenuItem,
  Dropdown,
  DropdownMenu,
  DropdownItem,
  // RadioGroup,
  // Radio,
  Image,
  Pagination,
  Tag,
  Descriptions,
  DescriptionsItem,
} from 'element-ui'

Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Button)
Vue.use(Row)
Vue.use(Col)
Vue.use(Link)
Vue.use(Tabs)
Vue.use(TabPane)
Vue.use(Card)
Vue.use(Dialog)
Vue.use(Menu)
Vue.use(Submenu)
Vue.use(MenuItem)
Vue.use(Dropdown)
Vue.use(DropdownMenu)
Vue.use(DropdownItem)
// Vue.use(Radio)
// Vue.use(RadioGroup)
Vue.use(Image)
Vue.use(Pagination)
Vue.use(Tag)
Vue.use(Descriptions)
Vue.use(DescriptionsItem)

Vue.use(Loading.directive)

Vue.prototype.$message = Message
Vue.prototype.$messageBox = MessageBox
