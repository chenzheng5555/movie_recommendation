export default {
  namespaced: true,
  state: {
    // 页面文档可视高度(随窗口改变大小)
    documentClientHeight: 0,
    // 侧边栏, 折叠状态
    sidebarFold: false,
    // 导航条, 布局风格, defalut(默认) / inverse(反向)
    navbarLayoutType: 'defalut',
    // 侧边栏, 布局皮肤, light(浅色) / dark(黑色)
    sidebarLayoutSkin: 'dark',
    //当前侧边栏名称
    menuActiveName: '',
    // 内容, 是否需要刷新
    contentIsNeedRefresh: false,
    // 主入口标签页
    mainTabs: [],
    mainTabsActiveName: ''
  },
  mutations: {
    updateDocumentClientHeight(state, height) {
      state.documentClientHeight = height
    },
    updateSidebarFold(state, fold) {
      state.sidebarFold = fold
    },
    updateMenuActiveName(state, name) {
      state.menuActiveName = name
    },
    updateContentIsNeedRefresh(state, status) {
      state.contentIsNeedRefresh = status
    },
    updateMainTabs(state, tabs) {
      state.mainTabs = tabs
    },
    updateMainTabsActiveName(state, name) {
      state.mainTabsActiveName = name
    },

  },
  actions: {
    addMainTabs({ commit, state }, route) {
      //console.log(route)
      if (route.meta.isTab) {
        // tab选中, 不存在先添加
        var tab = state.mainTabs.filter(item => item.name === route.name)[0]
        if (!tab) {
          tab = {
            menuId: route.meta.menuId || route.name,
            name: route.name,
            title: route.meta.title || route.params.title,
            //type: isURL(route.meta.iframeUrl) ? 'iframe' : 'module',
            //iframeUrl: route.meta.iframeUrl || '',
            params: route.params,
            query: route.query
          }
          state.mainTabs = state.mainTabs.concat(tab)
          //commit('updateMainTabs', new_mainTabs)
        }
        //commit('updateMainTabsActiveName', tab.name)
        state.menuActiveName = tab.menuId + ''
        state.mainTabsActiveName = tab.name
      }
    }
  }
}
