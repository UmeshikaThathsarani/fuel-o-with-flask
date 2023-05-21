import React from 'react';
import {
  HistoryOutlined,
  HomeOutlined,
  FundOutlined,
  CarOutlined
} from '@ant-design/icons';

export const ICONS = {
  home: <HomeOutlined />,
  prediction: <FundOutlined />,
  history: <HistoryOutlined />,
  rent: <CarOutlined />
};

export const PAGES = [
  {
    id: 1,
    name: 'Home',
    path: '/',
    icon: ICONS.home,
  },
  {
    id: 2,
    name: 'Prediction',
    path: '/prediction',
    icon: ICONS.prediction,
  },
  {
    id: 3,
    name: 'Activity History',
    path: '/history',
    icon: ICONS.history,
  },
  {
    id: 4,
    name: 'Rent A Car',
    path: '/rent',
    icon: ICONS.rent,
  }
];
